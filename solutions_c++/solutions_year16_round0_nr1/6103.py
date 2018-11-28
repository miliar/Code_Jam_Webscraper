#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long int
#define pb push_back
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%I64d",&x)
#define F first
#define S second
#define maxn 1000005
#define mod 1000000007

int mem[maxn];

int main(){

  int t;
  cin>>t;

  rep(i,t){
    int n,x,c=0;
    cin>>n;
    if(n==0){
      cout<<"Case #"<<i+1<<": INSOMNIA\n";
      continue; 
    }
    if(mem[n]){
      cout<<"Case #"<<i+1<<": "<<mem[n]<<"\n";
      continue;
    }
    set<int>s;
    while(s.size()<10){
      c++;
      x=c*n;
      while(x>0){
        s.insert(x%10);
        x/=10;
      }

    }
    mem[n]=c*n;
    cout<<"Case #"<<i+1<<": "<<c*n<<"\n";
    

  }

  return 0;
}