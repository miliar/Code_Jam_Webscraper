#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <sstream>

using namespace std;



int main() {
  int totalTc;
  cin >> totalTc;
  for(int tc = 1; tc <= totalTc; tc++) {
    int n; cin >> n;
    vector<string> strs(n);
    vector<int> idxs;
    for (int i=0; i<n; i++) { cin >> strs[i]; idxs.push_back(i); }
    /*
    set<char> forCheck1;
    bool flg = true;
    for (int i=0; i<n; i++) {
      if(!check1(strs[i],forCheck1)) {
	flg = false; break;
      }
    }
    for (int i=0; i<n; i++) {
      if(!check2(strs[i])){
	flg = false; break;
      }
    }
    if (!flg) {
      cout << "Case #" << tc << ": 0" << endl;
      continue;
    }
    */
    vector<string> exstrs(n,"");
    for (int i=0; i<n; i++) {
      string tmp = strs[i].substr(0,1);
      for (int j=1; j<(int)strs[i].size(); j++) {
	if (strs[i][j] != strs[i][j-1]) {
	  tmp += strs[i][j];
	}
      }
      exstrs[i] = tmp;
      /*
      if ((int)strs[i].size() > 1) {
	exstrs[i] = strs[i].substr(0,1) + strs[i].substr((int)strs[i].size()-1,1);
      } else {
	exstrs[i] = strs[i].substr(0,1);
      }
      */
    }
    int ans = 0;
    sort(idxs.begin(),idxs.end());
    do {
      string tmp = "";
      for (int i=0; i<n; i++){
	tmp += exstrs[idxs[i]];
      }
      vector<int> flgs(26,0);
      flgs[tmp[0]-'a'] = 1;
      bool tflg = true;
      for (int i=1; i<(int)tmp.size(); i++) {
	if(tmp[i] != tmp[i-1] && flgs[tmp[i]-'a']) {
	  tflg = false; break;
	}
	flgs[tmp[i]-'a'] = true;
      }
      if (tflg) ans ++;
    } while(next_permutation(idxs.begin(), idxs.end()));
    cout << "Case #" << tc << ": " << ans << endl;;
  }
  return 0;
}
