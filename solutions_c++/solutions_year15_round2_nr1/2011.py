#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <utility>
#include <map>
using namespace std;

size_t rev(size_t x)
{
    size_t ret = 0;
    while (x > 0) {
        ret = ret * 10 + (x % 10);
        x /= 10;
    }
    return ret;
}

typedef pair<size_t, size_t> Node;

bool cmpBy2nd(const Node& lhs, const Node& rhs)
{
    if (lhs.second != rhs.second)
        return lhs.second < rhs.second;
    return lhs.first < rhs.first;
}

size_t getAns(size_t N)
{
    static map<size_t, size_t> table;
    if (table[N] > 0)
        return table[N];
    table[0] = table[1] = 1;
    deque<Node> frontier;
    for(map<size_t, size_t>::const_iterator i = table.begin(); i != table.end(); ++i) {
        if (i->first != 0 && i->second != 0) {
            frontier.push_back(*i);
        }
    }
    sort(frontier.begin(), frontier.end(), cmpBy2nd);
    while(!frontier.empty()) {
        Node n = frontier.front();
        frontier.pop_front();
        //cerr << n.first << ", " << n.second <<endl;
        size_t reved = rev(n.first);
        if (table[reved] == 0) {
            table[reved] = n.second + 1;
            frontier.push_back(make_pair(reved, n.second+1));
        }
        if (table[n.first + 1] == 0) {
            table[n.first + 1] = n.second + 1;
            frontier.push_back(make_pair(n.first+1, n.second+1));
        }
        if (reved == N || n.first + 1 == N)
            break;
    }
    return table[N];
}

int main(void)
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        size_t N;
        cin >> N;
        cout << "Case #" << i << ": " << getAns(N) << endl;
    }
    return 0;
}
