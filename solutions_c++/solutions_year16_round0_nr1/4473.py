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

int main(void){

    int t,n,m,i,j,test;
    cin>>t;
    for(test=1;test<=t;++test){
       cin>>n;
       int ar[10];
       memset(ar,0,sizeof(ar));
       ll cnt = 1;
       ll num = n;
       while(1){
          if(cnt==5000000)
            break;
          ll dig = cnt*num;
          while(dig!=0){
            ar[dig%10] = 1;
            dig/=10;
          }
          int cc = 0;
          for(i=0;i<=9;++i)
            if(ar[i])
                cc++;
         if(cc==10)
            break;
         cnt++;
       }
       if(cnt!=5000000)
            cout<<"Case #"<<test<<": "<<cnt*num<<endl;
       else
            cout<<"Case #"<<test<<": "<<"INSOMNIA"<<endl;
    }
    return 0;
}
