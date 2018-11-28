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
freopen("D-small-attempt2.in","r",stdin);
   freopen("out3CAs.txt","w",stdout);
  int t,k,c,s;
  cin>>t;
  loop(r,1,t+1){
        cin>>k>>c>>s;
        cout<<"Case #"<<r<<": ";
        loop(i,1,k+1)cout<<i<<" ";
        cout<<endl;
  }

    return 0;
}
