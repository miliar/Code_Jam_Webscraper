#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm> 
#include <climits>
using namespace std;

vector<string> pos_strings(string s) {
  if (s.empty()) return vector<string>(1, "");
  
  string digits = "0123456789";
  vector<string> sub_res = pos_strings(s.substr(1));
  vector<string> res;
  for (int i = 0; i < sub_res.size(); i ++) {
    if (s[0] == '?') {
      for (char c: digits) 
	res.push_back(c + sub_res[i]);
    }
    else res.push_back(s[0] + sub_res[i]);
  }
  return res;
}

int main(int argc, char **argv) {
  std::string line;
  int T;
  cin >> T;
  std::getline(cin, line);
  for (int i = 0; i < T; i ++) {
    std::getline(cin, line);
    string C, J;
    int p = line.find(' ');
    C = line.substr(0, p);
    J = line.substr(p + 1);
    
    int size = C.size();
    
    vector<string> pos_c = pos_strings(C);
    vector<string> pos_j = pos_strings(J);
    
    sort(pos_c.begin(), pos_c.end());
    sort(pos_j.begin(), pos_j.end());
    // find the closest of pos_c and pos_p;
    int min_dist = INT_MAX;
    for (auto cs: pos_c) {
      for (auto js: pos_j) {
// 	cout << cs << " " << js << endl;
	if (abs(stoi(cs) - stoi(js)) < min_dist) {
	  min_dist = abs(stoi(cs) - stoi(js));
	  C = cs;
	  J = js;
	}
      }
    }
    cout << "Case #" << i + 1 << ": " << C << " " << J << endl;
  }
}


