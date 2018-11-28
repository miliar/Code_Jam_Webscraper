#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<set>
using namespace std;

#define ll long long
#define inf 1<<30
#define Mod 10000007
#define dbg printf("%c",a);
#define sz(a) (a).size()
int n,m;int ans;

int main()
{
    int i,j,k,T,cs=0;double C,X,F,f,t,wt,nwt;
    freopen("B-large.in","r",stdin);
    freopen("cookieout.txt","w",stdout);
    cin>>T;
    //while(scanf("%d",&n)==1)
    while(T--)
    {
        //scanf("%d",&x);
        cin>>C>>F>>X;
        f=2.0;t=0,nwt=0;wt=X/2;
        while(1)
        {

            nwt=C/f;
            f+=F;
            nwt+=X/f;
            //cout<<wt<<" "<<nwt<<endl;
            if(wt<nwt){t+=wt;break;}
            t+=C/(f-F);
            wt=X/f;
        }
        printf("Case #%d: %.7llf\n",++cs,t);

    }

    return 0;
}

