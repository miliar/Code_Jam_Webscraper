#include <bits/stdc++.h>
using namespace std;

int main(){
  #ifdef MY_PC
  freopen("i", "r", stdin); freopen("o", "w", stdout);
  #endif
  long long T,n;cin>>T;
  for (int t = 0; t < T; ++t)
  {
    int a[10]; memset(a,0,sizeof a);
    cin>>n;
    long long i; bool f =0;
    for (i = 1; i < 1000000; ++i)
    {
      string s = to_string(n*i);
      for(auto i:s)a[i-'0']=1;
      for (int j = 0; j < 10; ++j)
      {
        if(a[j]==0)break;
        if(j==9)f=1;
      }
      if(f)break;
    }
    cout<<"Case #"<<t+1<<": ";
    if(f)cout<<n*i<<endl;
    else cout<<"INSOMNIA"<<endl;
  }
}
  