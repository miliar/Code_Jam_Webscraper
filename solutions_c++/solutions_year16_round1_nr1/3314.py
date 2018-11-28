#include <bits/stdc++.h>
using namespace std;

int main(){
  int n;
  cin>>n;
  for(int q=1;q<=n;q++){

    string str,ans;
    cin>> str;
    ans+=str[0];
    for(int i=1;i<str.size();i++){
      string tmp=ans;
      if(ans[0]<=str[i])tmp=str[i]+ans; 
      else tmp=ans+str[i];
      ans=tmp;
    }

    cout << "Case #"<<q<<": "<<ans<<endl;
  }
  return 0;
}
