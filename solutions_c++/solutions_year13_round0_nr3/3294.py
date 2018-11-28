#include<iostream>
#include<string>
#include<sstream>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long ll;
ll T,a,b;
bool fine(ll x){
  stringstream ss;
  ss<<x;
  string str=ss.str();
  int len=str.length();
  int flg=1;
  for(int i=0;i<len-i-1;i++){
    if(str[i]!=str[len-i-1])flg=0;
  }
  if(flg==0)return false;
  return true;
}
int main(){
  cin>>T;
  for(int t=0;t<T;t++){
    ll ans=0;
    cin>>a>>b;
    ll start=(ll)sqrt((double)a);
    ll goal=(ll)sqrt((double)b);
    for(ll i=start;i<=goal;i++){
      if(fine(i)){
        ll temp=i*i;
        if(fine(temp)&&a<=temp&&temp<=b)ans++;
      }
    }
    cout<<"Case #"<<t+1<<": "<<ans<<endl;
  }

}
