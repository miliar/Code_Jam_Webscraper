#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <cassert>
using namespace std;

typedef pair< int, int > P;
map< P, P > trace;
const int BOUND = 100;

void go(queue< P > *q, int x, int y, int px, int py) {
    if (abs(x) > BOUND || abs(y) > BOUND
            || trace.find(P(x, y)) != trace.end())
        return;
    q->push(P(x, y));
    trace[P(x, y)] = P(px, py);
}

void bfs(int dest_x, int dest_y) {
    queue< P > *cur, *next;
    cur = new queue< P >();
    next = new queue< P >();
    go(cur, 0, 0, 0, 0);
    for (int n = 1; ; n++) {
        while (!cur->empty()) {
            const int x = cur->front().first,
                      y = cur->front().second;
            cur->pop();
            //cerr << n << " " << x << y << endl;
            if (x == dest_x && y == dest_y)
                return;
            go(next, x + n, y, x, y);
            go(next, x - n, y, x, y);
            go(next, x, y + n, x, y);
            go(next, x, y - n, x, y);
        }
        swap(next, cur);
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        trace.clear();
        cout << "Case #" << i << ": ";
        int x, y;
        cin >> x >> y;
        bfs(x, y);
        string ans;
        while (true) {
            //cerr << x << " " << y << " ";
            if (x == 0 && y == 0)
                break;
            auto t = trace[P(x, y)];
            int px = t.first;
            int py = t.second;
            if (x > px)
                ans += "E";
            else if (x < px)
                ans += "W";
            else if (y > py)
                ans += "N";
            else if (y < py)
                ans += "S";
            x = px;
            y = py;
        }
        reverse(ans.begin(), ans.end());
        cout << ans;
        cout << "\n";
    }
    return 0;
}
