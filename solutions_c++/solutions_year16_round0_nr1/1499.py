#include<bits/stdc++.h>
using namespace std;

bool f[15];

string to_s(int n){
  string res;
  stringstream ss;
  ss << n;
  ss >> res;
  return res;
}

bool is_end(){
  for(int i = 0;i < 10;++i){
    if(!f[i])return false;
  }
  return true;
}

void solve(int t){
  if(t == 0){
    puts("INSOMNIA");
    return;
  }
  for(int i = 0;i < 10;++i){
    f[i] = false;
  }
  int now = 0;
  while(true){
    now += t;
    string now_s = to_s(now);
    for(int i = 0;i < (int)now_s.size();++i){
      f[now_s[i] - '0'] = true;
    }
    if(is_end()){
      cout << now_s << endl;
      break;
    }
  }
  return;
}

int main(void){
  int n;
  cin >> n;
  for(int i = 0;i < n;++i){
    int t;
    cin >> t;
    cout << "Case #" << i+1 << ": ";
    solve(t);
  }
  return 0;
}
