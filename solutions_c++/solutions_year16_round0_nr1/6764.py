#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
  bool a[10];
  ll t,n,cnt,x,k,ans;
  cin>>t;
  for(int i=0;i<t;i++){
    cin>>n;
    for(int j=0;j<10;j++)a[j]=false;
    cnt=0;
    x=1;
    if(!n)cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
    else{
      while(1){
	k=ans=n*x;
	while(k){
	  if(!a[k%10])cnt++,a[k%10]=true;
	  k/=10;
	}
	if(cnt==10)break;
	x++;
      }
      cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
  }
  return 0;
}
