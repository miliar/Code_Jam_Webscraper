#include <bits/stdc++.h>
using namespace std;

int main(){
  int Q;
  cin>>Q;
  for(int q=0;q<Q;q++){
    string str;
    cin>>str;
    char ima=str[0];
    int ans=0;
    for(int i=1;i<str.size();i++)
      if(ima!=str[i]) ans++,ima=str[i];
    if(ima=='-') ans++;
    cout <<"Case #"<<q+1<<": "<<ans<<endl;
  }
  return 0;
}
