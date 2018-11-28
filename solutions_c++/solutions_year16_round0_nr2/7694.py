#include <iostream>
#include <string>

using namespace std;

int N;
string s;

void solve(int k){
  int res = 0;
  for(int i=0;i<s.size();i++)
    if(s[i] == '-'){
      if(!i) res ++;
      else if(s[i-1] == '+') res += 2;
    }
  cout << "Case #" << k << ": " << res << endl;
}

int main(int argc, char const *argv[]) {
  cin >> N;
  for(int i=0;i<N;i++){
    cin >> s;
    solve(i+1);
  }
  return 0;
}
