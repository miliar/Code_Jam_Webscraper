#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

struct Event {
    bool in;
    long long at, num;
    Event(bool a, long long b, long long c) {
        in = a, at = b, num = c;
    }
    bool operator <(const Event &e) const {
        if (at != e.at) return at < e.at;
        if (in != e.in) return in;
        return num > e.num;
    }
};

long long calc(long long n, long long from, long long to) {
    long long stations = to - from;
    if (stations == 0) return 0;
    assert(stations > 0);
    return stations * n - (stations * (stations + 1)) / 2;
}

int main() {
	int T = 1;
    int t;

    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;

        vector <Event> v;
        long long correct = 0;

        for (int i=0; i < m; ++i) {
            long long from, to, num;
            cin >> from >> to >> num;
            v.push_back(Event(true, from, num));
            v.push_back(Event(false, to, num));
            correct += num * calc(n, from, to);
//            cout << (num * calc(n, from, to)) << endl;
        }

        sort(v.begin(), v.end());

        stack < pair <long long, long long> > q;
        long long cheated = 0;
        
        for (int i=0; i < (int)v.size(); ++i) {
            if (v[i].in) {
                q.push(make_pair(v[i].at, v[i].num));
            }
            else {
                long long total = v[i].num;
                long long to = v[i].at;

                while (total > 0) {
                    assert(!q.empty());
                    long long from = q.top().first;
                    long long num = q.top().second;
                    assert(v[i].at >= from);
                    q.pop();

                    if (num > total) {
                        q.push(make_pair(from, num - total));
                        num = total;
                    }

                    cheated += num * calc(n, from, to);
                    total -= num;
                }
            }
        }

        cout << "Case #" << (T++) << ": " << (correct - cheated) << endl;
    }
	
	return 0;
}
