#include <iostream>
#include <algorithm>
using namespace std;
int main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;++t){
    int x,r,c;
    cin >> x >> r >> c;
    bool ans = false;
    if(x==1) ans = true;
    if(x==2 && (r*c)%2==0) ans=true;
    if(x==3 && (r*c)%3==0 && min(r,c)>1) ans=true;
    if(x==4 && (r*c)%4==0 && r*c>=12) ans=true;
    string s = (ans)?"GABRIEL":"RICHARD";
    cout << "Case #"<<t<<": "<<s<<endl;
  }
  return 0;
}
