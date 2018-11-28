#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long           LL;
typedef unsigned long long  ULL;
typedef unsigned int        uint;
typedef pair<int, int>      pii;
typedef pair<LL, LL>        pll;

const int INF = 0x3f3f3f3f;

priority_queue<pii> pq;

int main() {
    //ios::sync_with_stdio(false);
    int n, tot, T, cas = 1;
    cin >> T;
    while (T--) {
        tot = 0;
        while (!pq.empty()) pq.pop();
        cin >> n;
        for (int i = 0; i < n; i++) {
            int c;
            cin >> c;
            pq.push(mp(c, i));
            tot +=  c;
        }

        printf("Case #%d:", cas++);
        while (tot) {
            char s[5];
            int limit = tot >> 1;
            
            pii x = pq.top();
            pq.pop();
            s[0] = 'A' + x.second; s[1] = '\0';
            x.first--;
            tot--;
            if (x.first) pq.push(mp(x.first, x.second));
            
            limit = tot >> 1;
            x = pq.top();
            if (x.first > limit) {
                pq.pop();
                s[1] = 'A' + x.second; s[2] = '\0';
                x.first--;
                tot--;
                if (x.first) pq.push(mp(x.first, x.second));
            }

            cout << " " << s;
        }
        cout << endl;
    }
    return 0;
}
