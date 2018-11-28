#include<iostream>
#include<sstream>
#include<string>
#include<cmath>

using namespace std;

string int_to_string(int n){
  stringstream ss;
  ss << n;
  return ss.str();
}

bool check(const string& str){
  for(int i=0, j=str.size()-1; i < j; ++i, --j){
    if(str[i] != str[j]) return false;
  }
  return true;
}

int solve(double a, double b){
  double bg;
  if(modf(sqrt(a), &bg) != 0) ++bg;
  int ans = 0;
  for(int i = (int)bg; i <= sqrt(b); ++i){
    const string str1 = int_to_string(i);
    const string str2 = int_to_string(i*i);
    if(check(str1) && check(str2)) ++ans;
  }
  return ans;
}

int main(){
  int n;
  double a, b;
  cin >> n;
  for(int i=0; i<n; ++i){
    cin >> a >> b;
    cout << "Case #" << i+1 << ": " << solve(a, b) << endl;
  }
  return 0;
}
