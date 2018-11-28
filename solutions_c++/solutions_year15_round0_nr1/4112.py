#include <iostream>
#include <algorithm>
using namespace std;
int main(){
  int t;
  cin>>t;
  for(int j=1;j<=t;++j){
    int n;
    cin>>n;
    int ans=0;
    int num=0;
    string str; cin >> str;
    for(int i=0;i<=n;++i){
      int s = str[i]-'0';
      if(num>=i){
	num+=s;
      }
      else{
	ans+=i-num;
	num=i+s;
      }
    }
    cout<<"Case #"<<j<<": "<<ans<<endl;
  }
  return 0;
}
