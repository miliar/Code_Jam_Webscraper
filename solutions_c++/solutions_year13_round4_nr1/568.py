#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <climits>
#include <cassert>
#include <limits.h>
#include <iostream>
#include <algorithm>
#include <functional>
#define eps 1E-5
#define X first
#define Y second
#define ll long long
#define PB(x) push_back((x))
#define MP(x,y) make_pair((x),(y))
#define CLR(x) memset((x),0,sizeof((x)))
using namespace std;
const int                           Maxn=20005,Maxm=100005,Mo=1000002013;
const ll                            oo=LLONG_MAX>>2;
struct Tree{
    int l,r;
};
struct edge {
    int v,c,nt;
};
typedef pair<ll,ll>                     F;
typedef int                             IArr[Maxn];
typedef ll                              LArr[Maxn];
typedef double                          DArr[Maxn];



int                                     T,i,j,k,n,m,num;
LArr                                    l,r,p,suml,sumr;
int main()
{
    ios::sync_with_stdio(0);
    freopen("/Users/MAC/Desktop/Error202/Error202/1.in","r",stdin);
    freopen("/Users/MAC/Desktop/Error202/Error202/1.out","w",stdout);
    cin>>T;
    int tt=0;
    while(T--)
    {
        CLR(suml);
        CLR(sumr);
        cout<<"Case "<<"#"<<++tt<<": ";
        vector<ll> pos;
        cin>>n>>m;
        ll tot=0;
        for (i=1;i<=m;i++)
        {
            cin>>l[i]>>r[i]>>p[i];
            ll d=r[i]-l[i];
            tot=tot+(2*n-d+1)*d/2%Mo*p[i]%Mo;
            tot%=Mo;
            pos.PB(l[i]);
            pos.PB(r[i]);
        }
        sort(pos.begin(),pos.end());
        int num=(int)(unique(pos.begin(), pos.end())-pos.begin());
        for (i=1;i<=m;i++)
            for (j=0;j<num;j++)
                if (pos[j]==r[i])
                    sumr[j]+=p[i];
                else if (pos[j]==l[i])
                    suml[j]+=p[i];
        ll ans=0;
        stack<F> st;
        for (i=0;i<num;i++)
        {
            st.push(MP(i,suml[i]));
            while (sumr[i]) {
                F now=st.top();
                st.pop();
                ll cnt=min(now.Y,sumr[i]);
                ll d=pos[i]-pos[now.X];
                ans=ans+(2*n-d+1)*d/2%Mo*cnt%Mo;
                ans%=Mo;
                now.Y-=cnt;
                sumr[i]-=cnt;
                if (now.Y) st.push(now);
            }
        }
//        cout<<tot<<' '<<ans<<endl;
        cout<<(tot-ans+Mo)%Mo<<endl;
    }
}