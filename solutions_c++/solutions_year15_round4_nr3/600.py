#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;


bitset<2300> bt[22], bt1, bt2;

vector<string> vs[1100];


char ch[555555];

int main() {
    freopen("C:\\Users\\dd\\Downloads\\C-small-attempt1.in", "r", stdin);
    freopen("C:\\Users\\dd\\Downloads\\C-small-attempt1.out", "w", stdout);

    int Te; scanf("%d", &Te);
    for (int te = 1; te <= Te; te ++) {
        int N;
        scanf("%d", &N);
        gets(ch);
        map<string, int> mp;
        set<string> st2;

        for (int i = 0; i < N; i ++) {
            gets(ch);
            istringstream sin(ch);
            string s;
            vs[i].clear();
            while (sin >> s) {
                vs[i].push_back(s);
                mp[s] = 0;
                if (i >= 2) {
                    st2.insert(s);
                }
            }
        }
        int i = 0;
        for (map<string, int>::iterator it = mp.begin(); it != mp.end(); ++ it) {
            mp[it->first] = i ++;
        }
        for (int i = 0; i < N; i ++) {
            bt[i].reset();
            for (int j = 0; j < vs[i].size(); j ++) {
                bt[i].set(mp[vs[i][j]]);
            }
        }

             int ans = 100000000;
                for (int s = 0; s < (1 << N); s ++) {
                    if ((s & 3) != 1) continue;
                    bt1.reset();
                    bt2.reset();
                    for (int i = 0; i < N; i ++) {
                        if (s & (1 << i)) {
                            bt1 |= bt[i];
                        } else {
                            bt2 |= bt[i];
                        }
                    }

                    ans = min(ans, (int)(bt1 & bt2).count());
                }

        printf("Case #%d: %d\n", te, ans);

    }
    //system("pause");
}