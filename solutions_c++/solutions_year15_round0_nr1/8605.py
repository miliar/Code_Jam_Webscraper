#include<bits/stdc++.h>
using namespace std;

#define s(n) scanf("%d",&n)
#define sfor(n) for(int i=1; i<=n; i++)
#define aforb(a,b) for(int i=a; i<=b; i++)
#define pf printf
#define ll long long
#define ull unsigned ll
#define MOD 1000000007
#define pub push_back
#define pob pop_back
#define mem(a,v) memset(a,v,sizeof(a))
#define gcd(x,y) __gcd(x,y)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define multimod2(a,b) ((a%MOD)*(b%MOD))%MOD
#define multimod3(a,b,c) ((a%MOD)*(b%MOD)*(c%MOD))%MOD
#define MIN(a, b) (a<b?a:b)
#define MAX(a, b) (a>b?a:b)
#define s2(n,m) scanf("d",&n,&m)

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outputLarge.out","w",stdout);
    int standing,friends,tc,n,ttc;
    char num;
    s(tc);
    for(int i=1; i<=tc; ++i)
    {
        friends=standing=0;
        s(n);
        for(int j=0; j<=n; ++j)
        {
            cin>>num;
            ttc=num-48;
          //  cout<<ttc<<endl;
           // cout<< standing<< ' '<<j<<' '<<friends<<endl;
            if(standing >= j ) standing += ttc;
            else
            {

                friends+=j-standing;
                standing+=(j-standing)+ttc;
                //cout<<"ELSE"<<j-standing<<' '<<standing<<endl;
            }

        }
        pf("Case #%d: %d\n",i,friends);

    }



    return 0;
}
