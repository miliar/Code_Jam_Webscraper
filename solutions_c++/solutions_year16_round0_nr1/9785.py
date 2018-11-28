#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
typedef long long ll;
using namespace std;
int T;
bool check(bool arr[]){
  bool ans=1;
  for(int i=0;i<10;i++)
    ans&=arr[i];
  return ans;
}
int main(){
  cin>>T;
  for(int t=0;t<T;t++){
    long long n;
    cin>>n;
    if(n==0){
      printf("Case #%d: INSOMNIA\n",t+1);
      continue;
    }
    bool arr[10];
    for(int i=0;i<10;i++)
      arr[i]=0;
    for(ll i=n;i<10000000;i+=n){
      ll tmp=i;
      while(tmp>0){
	arr[tmp%10]=1;
	tmp/=10;
      }
      // cout<<i<<":  ";
      //for(int j=0;j<10;j++)
      //cout<<arr[j]<<" ";
      //cout<<endl;
      if(check(arr)){
	cout<<"Case #"<<t+1<<": "<<i<<endl;
	break;
      }
    }

  }
  return 0;
}
