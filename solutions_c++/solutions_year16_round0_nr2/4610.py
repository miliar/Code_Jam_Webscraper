#include <bits/stdc++.h>

using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define pd(x) printf("%d",x)
#define pull(x) printf("%llu",x)
#define pll(x) printf("%lld",x)

#define pn() printf("\n")
#define loop(i, a, b) for (int i = int(a); i < int(b); i++)
#define MAXN 1000005
typedef long long int ll;
typedef unsigned long long int ull;

int main()
{
   freopen("B-large.in","r",stdin);
   freopen("out_large2CAs.txt","w",stdout);
   int t,n;
   ll cnt;
   string s;
   cin>>t;
   loop(k,1,t+1){
      cin>>s;
      n=s.size();
      cnt=0;
      for(int i=n-1;i>=0;i--){
            if(s[i]=='-'){
                cnt++;
                for(int j=i;j>=0;j--){
                    s[j]=(s[j]=='-'?'+':'-');
                }
            }
      }
      cout<<"Case #"<<k<<": "<<cnt<<endl;
   }



    return 0;
}




