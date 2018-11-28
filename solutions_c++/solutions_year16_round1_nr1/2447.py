#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int main(){
  ios_base::sync_with_stdio(0);
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    string s;
    cin>>s;
    string res = "";
    for(char c:s){
      if(res=="")
	res += c;
      else if(c >= res[0])
	res = c + res;
      else
	res = res + c;
    }
    cout<<"Case #"<<t<<": "<<res<<endl;
  }
  return 0;
}
