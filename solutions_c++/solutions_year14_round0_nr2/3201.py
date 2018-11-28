#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits>
#include<stack>
#include<queue>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
using namespace std;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n)  for(int i=0;i<n;i++)
#define fu(i,a,n) for(int i=a;i<=n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define all(a)    a.begin(),a.end()
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define gl(n) cin >> n
#define pi(n) printf("%d",n)
#define pl(n) cout << n
#define ps printf(" ")
#define pn printf("\n")
int main()
{
    //freopen("B-small-attempt0.in","rt",stdin);
    //freopen("B-small-attempt0.out","wt",stdout);
    freopen("B-large.in","rt",stdin);
    freopen("B-large-attempt0.out","wt",stdout);
    int T;
    si(T);
    for(int t=1;t<=T;t++)
    {
        double C,F,X,cc,tt=0.0000000,tra,trb;
        cin>>C>>F>>X;
        cc=2,tt=0;
        while(1)
        {
            tra=(X)/cc;
            trb=C/cc;
            trb+=X/(cc+F);
            if(tra <= trb)
            {
                tt+=tra;
                break;
            }
            else
            {
                tt+=C/cc;
                cc+=F;
            }
        }
        //printf("Case #%d: %lf\n",t,tt);
        cout<<"Case #"<<t<<":"<<" ";
        cout << std::fixed;
        cout<<setprecision(7)<<tt<<endl;
    }
    return 0;
}
