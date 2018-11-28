#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define fora(x,y,z) for(int x=y;x<=(z);x++)
#define PNL printf("\n")
#define FL(a,n,x) fill(a,a+n,x)
#define pii pair<int,int>
#define F first
#define S second
#define mp make_pair
#define MOD 1000000007
#define debug(x) cout<<"here"<<x<<endl;

int main(){
   freopen("Input11S.in","r",stdin);
   freopen("Output11S.txt","w",stdout);
   int te,c,k,s;
   si(te);
   int ts=0;
   while(te--){
   ts++;
   si(k); si(c); si(s);
   cout<<"Case #"<<ts<<": ";
   fora(i,1,k)
   cout<<i<<" ";
   PNL;
   }
   return 0;
}
