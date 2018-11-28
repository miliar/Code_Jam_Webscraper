#include<iostream>


using namespace std;

string helper(string s, string rs) {
  if(rs.length() == 0) return s;
  
  string left =  helper(rs[0] +  s , rs.substr(1));
  string right = helper(s + rs[0] , rs.substr(1));

  return left < right ? right : left;
};

string solve(string input) {
  return helper(input.substr(0,1), input.substr(1));
}

int main() {
  int T;
  cin >> T;
  for(int t=0;t < T; ++t) {

    string input;
    cin >> input;
    string result = solve(input);
    cout<<"Case #" << t + 1 << ": " << result <<endl;
  }
}
