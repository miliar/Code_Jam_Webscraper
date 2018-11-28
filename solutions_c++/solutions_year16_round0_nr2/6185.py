#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long int
#define pb push_back
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%I64d",&x)
#define F first
#define S second
#define maxn 100005
#define mod 1000000007

int main(){

  int t;
  cin>>t;
  rep(tc,t){
    string s;
    cin>>s;
    int ans=0;
    for(int i=s.size()-1;i>=0;i--){
      if(s[i]=='+')continue;
      if(s[0]=='-'){
        
        ans++;
        for(int j=0;j<=i;j++){
          if(s[j]=='-')s[j]='+';
          else s[j]='-';
        }
        
        for(int j=0;j<=i/2;j++){
          swap(s[j],s[i-j]);
        }
        
      }
      else{
        int m=0;
        while(s[m]=='+')m++;
        ans++;
        for(int j=0;j<m;j++)s[j]='-';
        ans++;

        for(int j=0;j<=i;j++){
          if(s[j]=='-')s[j]='+';
          else s[j]='-';
        }
        for(int j=0;j<=i/2;j++){
          swap(s[j],s[i-j]);
        }
        
      }
    }
    cout<<"Case #"<<tc+1<<": "<<ans<<"\n";
  }

  return 0;
}