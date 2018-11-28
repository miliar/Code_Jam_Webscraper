#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cassert>
#include <ctime>
#include <queue>
#include <map>
#include <set>
#include <climits>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef pair<int, int> PII;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(auto it=(c).begin();it!=(c).end();++it)
#define FILLCHAR(a, x) memset(a, x, sizeof(a))
#define SZ(x) ((int) (x).size())
#define ALL(x) (x).begin(), (x).end()

map<pair<vector<int>, int>, bool> dict;

bool canDo(vector<int>& pq, int target)
{
    pair<vector<int>, int> pp = make_pair(pq, target);
    if (dict.count(pp)) return dict[pp];
    if (pq.back() <= target) return true;

    bool ret = false;
    for (int i = 1; i < pq.back(); i++) {
        vector<int> next_pq = pq;
        next_pq.pop_back();
        next_pq.push_back(i);
        next_pq.push_back(pq.back() - i);
        sort(next_pq.begin(), next_pq.end());
        if (canDo(next_pq, target - 1)) {
            ret = true;
            break;
        }
    }

    dict[pp] = ret;
    return ret;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        dict.clear();
        int D;
        cin >> D;
        vector<int> P;
        for (int j = 0; j < D; j++) {
            int tmp;
            cin >> tmp;
            P.push_back(tmp);
        }

        sort(P.begin(), P.end());
        int left = 1;
        int right = P.back();

        while (left < right) {

            int mid = (left + right) / 2;

            if (canDo(P, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        cout << "Case #" << i + 1 << ": " << left << endl;
/*
        for (int j = 1; j <= P.top(); j++) {
            if (canDo(P, j)) {
                cout << "Case #" << i + 1 << ": " << j << endl;
                break;
            }
        }*/
    }
}
