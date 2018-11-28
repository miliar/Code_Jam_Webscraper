#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define ii pair<int,int>
#define vi vector<int>
#define _(A,v) memset(A,v,sizeof(A))
#define all(A) (A).begin(),(A).end()
#define forn(i,n)for(int i=0;i<n;i++)
#define foreach(it,A) for(__typeof((A).begin())it=(A).begin();it!=(A).end();it++)
#define endl '\n'
#define dbg(xD) cerr<<" >"<<__LINE__<<": "<<#xD<<" = "<<xD<<endl
#define fast_io ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

int foo(string S){
   char c=S[0];
   int n=1;
   for(int i=1;i<S.size();i++){
      if(S[i]!=c){
         n++;
         c=S[i];
      }
   }
   return n;  
}

int main(){
   freopen("B-large.in","r",stdin);
   freopen("B-large.out","w",stdout);
   int tc,n;
   string S;
   cin>>tc;
   for(int i=1;i<=tc;i++){
      cin>>S;
      n=foo(S);
      cout<<"Case #"<<i<<": ";
      if(n%2==0){
         if(S[0]=='+')cout<<n<<endl;
         else cout<<n-1<<endl;
      }
      else{
         if(S[0]=='+')cout<<n-1<<endl;
         else cout<<n<<endl;
      }
   }
    
   return 0;
}