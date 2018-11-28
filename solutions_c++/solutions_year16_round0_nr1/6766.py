#include <bits/stdc++.h>
using namespace std;

int main(){
  bool f[10];
  int t;

  cin>>t;
  for(int j=0;j<t;j++){
    long long n,ans;
    cin>>n;
    cout<< "Case #"<<j+1<<": ";
    if(n==0) cout<<"INSOMNIA"<<endl;
    else {
      memset(f,0,sizeof(f));
      for(int i=1;(f[0]&f[1]&f[2]&f[3]&f[4]&f[5]&f[6]&f[7]&f[8]&f[9]) ==0;i++){
	long long tmp;
	ans = tmp = n*i;
	for(;tmp>0;tmp/=10) f[tmp%10]=1;
      }
      cout<<ans<<endl;
    }
  }
    return 0;
}
