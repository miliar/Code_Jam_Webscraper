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
   freopen("Output.txt","w",stdout);
   int te,n;
   si(te);
   int ts=0;
   while(te--){
   ts++;
   set<int> st;
   si(n);
   if(n==0){
   cout<<"Case #"<<ts<<": "<<"INSOMNIA"<<endl;
   continue;
   }

   ll m=0;
   while(m <= INT_MAX && st.size()<10){
   m=m+n;
   ll tmp=m;
   while(tmp!=0){
   int x=tmp%10;
   st.insert(x);
   tmp=tmp/10;
   }
   }
   cout<<"Case #"<<ts<<": "<<m<<endl;
   }
   return 0;
}
