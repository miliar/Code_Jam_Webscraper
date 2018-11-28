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
   freopen("InputL.in","r",stdin);
   freopen("OutputL.txt","w",stdout);
   int te;
   char str[10000];
   si(te);
   int ts=0;
   while(te--){
   ts++;
   scanf(" %s",str);
   int n=strlen(str);
   int ans=0;
   if(str[0]=='-')
   ans++;
   fora(i,1,n-1)
   if(str[i-1]=='+' && str[i]=='-')
   ans+=2;
   cout<<"Case #"<<ts<<": "<<ans<<endl;
   }
   return 0;
}
