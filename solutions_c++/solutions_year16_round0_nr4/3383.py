#include<bits/stdc++.h>
#define pn() printf("\n")
#define ps() printf(" ")
#define si(x) scanf("%d",&x)
#define pi(x) printf("%d",x)
#define sll(x) scanf("%I64d",&x)
#define pll(x) printf("%I64d",x)
#define sc(x) scanf("%c",&x)
#define pc(x) printf("%c",x)
#define sf(x) scanf("%f",&x)
#define pf(x) printf("%f\n",x)
#define sd(x) scanf("%lf",&x)
#define pd(x) printf("%.9lf\n",x)
#define sld(x) scanf("%Lf",&x)
#define pld(x) printf("%.9Lf\n",x)
#define MOD 1000000007
#define ll long long
#define eps 1e-10
using namespace std;

ll po(ll a,ll b){
  ll ans = 1;
  while(b){
     if(b&1)
        ans = ans*a;
     a = a*a;
     b/=2;
  }
  return ans;
}

int main(void){

    int t,n,m,i,j,test;
    ll k,c,ss;
//    precompute();
    cin>>t;
    for(test=1;test<=t;++test){
            cin>>k>>c>>ss;
            cout<<"Case #"<<test<<": ";
             ll st = 1;
             ll add = po(k,c-1);
             if(c>=2)
                add+=po(k,c-2);
             if(c>=3)
                add+=1;
             for(i=1;i<=ss;++i){
                cout<<st+(i-1)*add<<" ";

             }
            cout<<endl;


    }
    return 0;
}
