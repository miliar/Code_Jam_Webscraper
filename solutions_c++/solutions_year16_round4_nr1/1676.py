#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MOD 1000000007



int main() {
int TT;cin >>TT;
for(int ncase=1;ncase<=TT;ncase++){
  int ans=0;
  int N,P,R,S;
  cin >>N>>R>>P>>S;
  std::string s=string(P,'P')+string(R,'R')+string(S,'S');
//  cout<<s;
//  cout<<s.length();
  std::sort(s.begin(), s.end());
  bool possible;
  do {
    string t=s;
    possible=true;
    while(t.length()>1){
      string u;
      for(int i=0;i<t.length();i+=2){
        if(t[i]>t[i+1])swap(t[i],t[i+1]);
        if(t[i]==t[i+1]){possible=false;break;}
        if(t[i]=='P' && t[i+1]=='R')u+='P';
        else if(t[i]=='P' && t[i+1]=='S')u+='S';
        else if(t[i]=='R' && t[i+1]=='S')u+='R';
      }
      if(possible)
        t=u;
      else
        break;
    }
    if(possible)
      break;
    ans++;
      //std::cout << s << '\n';
  } while(std::next_permutation(s.begin(), s.end()));
  //cout << "Case #"<<setprecision(10)<<ncase<<": "<<ans<<endl;
  if(possible)
    cout << "Case #"<<ncase<<": "<<s<<endl;
  else
    cout << "Case #"<<ncase<<": "<<"IMPOSSIBLE"<<endl;
}

}
