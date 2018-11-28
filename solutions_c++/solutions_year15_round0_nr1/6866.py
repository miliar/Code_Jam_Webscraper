#include <bits/stdc++.h>
using namespace std;
int main(){
  int T,n,c,y;
  cin>>T;
  for(int k=1; k<=T; k++) {
    string cad;
    cin>>n;
    cin>>cad;
    c=0,y=0;
    for(int i=0; i<cad.length(); i++) {
      int x=(int)cad[i]-'0';
      if(x==0) continue;
      if(c>=i)
	c+=x;
      else{
	y+=(i-c);
	c+=(i-c);
	c+=x;
      }
    }
    cout<<"Case #"<<k<<": "<<y<<endl;
  }
  return 0;
}
