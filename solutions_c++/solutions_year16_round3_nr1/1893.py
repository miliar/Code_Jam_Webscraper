#include <iostream>
#include<utility>
#include<queue>

using namespace std;

int main() {
    int test;
    cin >> test;
    for (int t=1; t<=test; ++t) {
        priority_queue<pair<int, char> > pr;
        pair<int, char> p;
        int n, s = 0;
        cin >> n;
        for (int i=0; i<n; ++i) {
            p.second = 'A' + i;
            cin >> p.first;
            s += p.first;
            pr.push(p);
        }
        cout << "Case #" << t << ":";
        if (s % 2 == 1) {
            p = pr.top();
            pr.pop();
            --p.first;
            cout << " " << p.second;
            if (p.first > 0) pr.push(p);
        }
        while (pr.size() > 0) {
            pair<int, char> p1, p2;
            p = pr.top();
            pr.pop();
            p1 = p;
            --p1.first;
            if (p1.first > 0) pr.push(p1);

            p = pr.top();
            pr.pop();
            p2 = p;
            --p2.first;
            if (p2.first > 0) pr.push(p2);

            cout << " " << p1.second << p2.second;
        }
        cout << endl;
    }
    return 0;
}
