#pragma comment(linker, "/STACK:1024000000,1024000000")
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<sstream>
#include<string>
#include<bitset>
#include<utility>
#include<numeric>
#include<assert.h>

using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define repn(i,a,n) for (int i=a;i<=n;i++)

typedef long long LL;
typedef unsigned long long ULL;

const LL LINF = (1LL <<60);
const int INF = 0x3f3f3f3f;

const int NS = 20010;
const int MS = 210;
const int MOD = 1000000007;
const double PI = acos(-1.0);

#define form(_i, L, R) for (int (_i) = L; (i) <= (R); ++(_i))
inline bool isdigit(char ch){return ((ch<='9')and(ch>='0'));}
inline void read(int &x){
    char ch;
    bool flag=false;
    for (ch=getchar();!isdigit(ch);ch=getchar()) if (ch=='-') flag=true;
    for (x=0;isdigit(ch);x=x*10+ch-'0',ch=getchar());
    x=flag?-x:x;
}

string cur, nxt;

int main()
{
  //  ios::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif
    int nCase;
    int ans;
    while(cin>>nCase)
    {
        for(int nT = 1; nT <= nCase; nT++)
        {
            cin>>cur;
         //   cout<<"cur = "<<cur<<endl;
            int iLen = cur.size();
            nxt = "A";
            nxt[0] = cur[0];
        //    cout<<"nxt = "<<nxt<<endl;
            for(int i = 1; i < iLen; i++)
            {
                if(cur[i] >= nxt[0])
                {
                    nxt = cur[i] + nxt;
                }
                else
                {
                    nxt = nxt + cur[i];
                }
            }
            nxt[iLen] = '\0';
            cout<<"Case #"<<nT<<": ";
            cout<<nxt<<endl;
        }
    }
    return 0;
}

/*
for(int nT = 1; nT <= nCase; nT++)
        {
            cin>>cur;
            int iLen = strlen(cur);
            nxt[0] = cur[0];
            for(int i = 1; i < iLen; i++)
            {
                if(cur[i] >= nxt[0])
                {
                    nxt = cur[i] + nxt;
                }
                else
                {
                    nxt += cur[i];
                }
            }
            nxt[iLen] = '\0';
            cout<<"Case #"<<nT<<": ";
            cout<<nxt<<endl;
        }
*/
//   __typeof(val.begin()) it = val.begin();
// ios::sync_with_stdio(false);
// cout<<setprecision(30);
