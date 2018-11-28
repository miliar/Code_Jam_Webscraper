#include <stdio.h>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
#include <fstream>
#include <sstream>

using namespace std;

#define MAXN 100010

#define INF 1e20
#define eps 1e-8
#define mod 998244353

int T;

int n;

string s1, s2, tmp;
string s[23];

int col[5000];
int tot;

map <string, int> to;

set <int> p1, p2;
set <int> ps[23];
set <int>::iterator it;

vector <int> p1_, p2_;
vector <int> ps_[23];

int main()
{
    freopen("pro.in","r",stdin);
    freopen("pro.out","w",stdout);

    ios::sync_with_stdio(0);

    int cas = 1;

    cin>>T;

    while(T--) {
        p1.clear();
        p2.clear();
        to.clear();
        p1_.clear();
        p2_.clear();

        tot = 0;

        cin>>n;
        getline(cin, s1);
        getline(cin, s1);
        getline(cin, s2);

        istringstream st1(s1);

        while(st1 >> tmp) {
            if(to[tmp] == 0) to[tmp] = ++tot;
            p1.insert(to[tmp]);
        }

        istringstream st2(s2);
        while(st2 >> tmp) {
            if(to[tmp] == 0) to[tmp] = ++tot;
            p2.insert(to[tmp]);
        }

        int m = n - 2;

        for(int i = 0; i < m; i++) {
            getline(cin, s[i]);
            ps[i].clear();
            ps_[i].clear();

            istringstream st(s[i]);
            while(st >> tmp) {
                if(to[tmp] == 0) to[tmp] = ++tot;
                ps[i].insert(to[tmp]);
            }
        }

        for(it = p1.begin(); it != p1.end(); ++it) {
            p1_.push_back(*it);
        }

        for(it = p2.begin(); it != p2.end(); ++it) {
            p2_.push_back(*it);
        }

        for(int i = 0; i < n; i++) {
            for(it = ps[i].begin(); it != ps[i].end(); ++it) {
                ps_[i].push_back(*it);
            }
        }


        int ans = -1;
        for(int i = 0; i < (1 << m); i++) {
            memset(col,0,sizeof(col));

            for(int j = 0; j < p1_.size(); j++) {
                col[p1_[j]] |= 1;
            }

            for(int j = 0; j < p2_.size(); j++) {
                col[p2_[j]] |= 2;
            }

            for(int j = 0; j < m; j++) {
                for(int u = 0; u < ps_[j].size(); u++) {
                    if(i & (1 << j)) col[ps_[j][u]] |= 1;
                    else col[ps_[j][u]] |= 2;
                }
            }

            int sum = 0;
            for(int j = 1; j <= tot; j++) {
                if(col[j] == 3) sum++;
            }

            if(ans == -1) ans = sum;
            else ans = min(ans, sum);
        }

        printf("Case #%d: %d\n", cas++, ans);
    }

    return 0;
}
