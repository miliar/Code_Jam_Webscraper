using namespace std;
#include <algorithm>
#include <iostream>

string f(string s){
  if (s == "R") return "RS";
  if (s == "P") return "PR";
  if (s == "S") return "PS";

  int len = s.length();
  string left  = s.substr(0, len/2);
  string right = s.substr(len/2);

  string option1 = f(left) + f(right);
  string option2 = f(right) + f(left); 
  return min(option1, option2);
}

string ff(int n, string s){
  if (n == 1) return f(s);
  return ff(n-1, f(s));
}

int main(){
  int T;
  cin >> T;
  for (int t=1; t<=T; t++){
    int n,r,p,s;
    cin >> n >> r >> p >> s;
    string out = "IMPOSSIBLE";
    int rs, ps;
    string try1;
    try1 = ff(n, "R");
    rs = count(try1.begin(), try1.end(), 'R');
    ps = count(try1.begin(), try1.end(), 'P');
    if ((r == rs) && (p == ps)) out = try1;
    try1 = ff(n, "P");
    rs = count(try1.begin(), try1.end(), 'R');
    ps = count(try1.begin(), try1.end(), 'P');
    if ((r == rs) && (p == ps)) out = try1;
    try1 = ff(n, "S");
    rs = count(try1.begin(), try1.end(), 'R');
    ps = count(try1.begin(), try1.end(), 'P');
    if ((r == rs) && (p == ps)) out = try1;
    
    cout << "Case #" << t << ": " << out << endl;
  }

}

