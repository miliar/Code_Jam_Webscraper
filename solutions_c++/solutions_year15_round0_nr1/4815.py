#include<iostream>
#include<cstring>
using namespace std;

int main(){
  int T,ans;
  cin>>T;
  for(int i=1;i<=T;i++){
    int l,cum;
    string s;
    cin>>l>>s;
    cum = 0, ans = 0;
    for(int j=0;j<=l;j++){
      int c = s[j] - '0';
      if (cum < j){
        ans = ans + (j - cum);
        cum = cum + (j - cum);
      }
      cum = cum + c;
    }

    cout<<"Case #"<<i<<": "<<ans<<endl;
  }
  return 0;
}
