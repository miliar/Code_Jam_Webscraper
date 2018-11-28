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
    string s;
    cin >> s;
    // -が先頭にある -> -を+にする
    // +が先頭にあり、かつ-が後ろにある, +を-にする
    // これを繰り返すだけ
    deque<int> v;
    int cnt = 0;
    for(int i=0;i<(int)s.size();i++){
      if(cnt == 0){
        cnt++;
      }
      else{
        if(s[i-1]!=s[i]){
          if(s[i-1]=='-')cnt*=-1;
          v.push_back(cnt);
          cnt = 0;
        }
        cnt++;
      }
    }
    if(cnt!=0){
      if(s[(int)s.size()-1]=='-')cnt*=-1;
      v.push_back(cnt);
    }
    int ans = 0;
    while(v.size()!=1){
      int tmp = v[0];
      v.pop_front();
      v[0] -= tmp;
      ans++;
    }
    if(v[0] < 0){
      ans++;
    }
    cout<<ans<<endl;
  }
  
  return 0;
}
