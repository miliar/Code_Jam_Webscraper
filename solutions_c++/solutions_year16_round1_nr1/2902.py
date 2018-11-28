#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}


int main(){
  fastStream();
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    cout << "Case #" << t << ": ";
    string S;
    cin>>S;
    string cur;
    for(int i = 0; i < (int)S.size(); i++){
      string tmp1 = S[i] + cur;
      string tmp2 = cur + S[i];
      if(tmp1 > tmp2){
        cur = tmp1;
      }
      else{
        cur = tmp2;
      }
    }
    cout<<cur<<endl;
  }
  
  return 0;
}
