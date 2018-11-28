
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>
#include <bitset>
#define INF 111111111
#define eps 1e-9
using namespace std;
char s[22][11111];
map<string, int> h;
map<int, int> g;
vector<int> v[22];
bitset<4000> a[22];
int cc;
void work(int x)
{
    string ss = string(s[x]);
    stringstream sr;
    sr<<ss;
    string r;
    while(sr>>r)
    {
        if (h.find(r) == h.end()) h[r] = ++cc;
        int id = h[r];
        v[x].push_back(id);
    }
}
int main()
{
    int T, cas = 0, i, j, n, m, k;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin>>T;
    while(T--)
    {
        h.clear();
        cc = 0;
        scanf("%d\n", &n);
        for(i = 0; i < 21; i++) v[i].clear();
        for(i = 0; i < 21; i++) a[i].reset();

        for(i = 0; i < n; i++)
        {
            gets(s[i]);
            work(i);
        }
        for(i = 0; i < n; i++){
            for(k = 0; k < v[i].size(); k++)
                a[i].set(v[i][k]);
//            cout<<a[i].count()<<endl;
        }
        int ans = (1<<29);

        for(i = 0; i < (1 << (n - 2)); i++)
        {
//            for(j = 0; j < n; j++)
//                a[j].reset();
            bitset<4000> a1,a2;
            a1.reset();
            a2.reset();
            int now = 0;
            a1 = a[0];
            a2 = a[1];
//            for(j = 0; j < v[0].size(); j++)
//                a1.set(v[0][j]);
//            for(j = 0; j < v[1].size(); j++)
//            {
//                a2.set(v[1][j]);
//            }
            for(j = 0; j < n - 2; j++)
                if ((1 << j) & i)
                {
                    a2 = (a2 | a[j + 2]);
                }
                else
                {
                    a1 = (a1 | a[j + 2]);
                }
//            cout<<i<<"  "<<(int)(a1 & a2).count()<<endl;
            ans = min(ans, (int)(a1 & a2).count());
        }
        printf("Case #%d: ", ++cas);
        printf("%d\n", ans);
    }
    return 0;
}
