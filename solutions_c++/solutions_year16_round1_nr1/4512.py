#include <bits/stdc++.h>
using namespace std;
string S;
string ans = "A";
int num_of_case = 1;

void output(int v){
  cout << "Case #" << num_of_case++ << ": " << v << endl;
}
void output(string v){
  cout << "Case #" << num_of_case++ << ": " << v << endl;
}

void func(string str, int i){
  if(i == S.length()){
    ans = max(ans, str);
    return;
  }
  func(str+S.substr(i, 1), i+1);
  func(S.substr(i, 1)+str, i+1);
}

int main(void){
  int T;
  cin >> T;
  while(T--){
    ans = "A";
    cin >> S;
    func(string(1,S[0]), 1);
    output(ans);
  }
  return 0;
}
