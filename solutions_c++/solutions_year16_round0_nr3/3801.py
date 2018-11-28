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

int ans;
double dp[11][31];
void precompute(){
   int i,j;
   for(i=2;i<=10;++i)
        for(j=0;j<=30;++j){
          if(j==0)
            dp[i][j] = 1;
          else
            dp[i][j] = dp[i][j-1]*i;
        }
}

double checkprime(double num){

    ll nu = (ll)(num);
  for(ll i=2;i*i<=nu;++i){
     if(nu%i==0)
        return i;
  }
    return 0;
}

int main(void){

    int t,n,m,i,j,test,k,l;
    precompute();
    cin>>t;
    for(test=1;test<=t;++test){
            cin>>n>>m;

            cout<<"Case #"<<test<<":"<<endl;
            int cnt = 0;
            for(j=0;j<min(2000000,(1<<(n-2)));++j){
                if(cnt==m)
                    break;
                int ff = 1;
                vector<ll>sol;
               for(k=2;k<=10;++k){
                  double num = dp[k][n-1]+1;
                  for(l=0;l<n-2;++l)
                        if(j & (1<<l))
                            num+=dp[k][l+1];
                    ll vv = checkprime(num);
                    if(vv==0){
                      ff = 0;
                      break;
                    }else
                        sol.push_back(vv);
               }
               if(ff){
                 cnt++;
                 cout<<"1";
                 for(l=n-3;l>=0;--l)
                    if(j & (1<<l))
                        cout<<"1";
                    else
                        cout<<"0";
                 cout<<"1 ";
                 for(l=0;l<sol.size();++l)
                    cout<<sol[l]<<" ";
                 cout<<endl;
                 sol.clear();
               }
            }

    }
    return 0;
}
