#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

class Party {
public:
  int num;
  string group;
  Party(int _num, string _group):
    num(_num), group(_group) {}
  bool operator<(const Party &s) const {
    return num > s.num;
  }
};


int main() {
  int tc; cin >> tc;
  for (int t = 1; t <= tc ; t++) {
    int n; cin >> n;

    vector<Party> parties;
    int all_num = 0, all_party = 0;
    for (int i = 0; i < n; i++) {
      int num; cin >> num;
      string g(1, (char)('A' + i));
      parties.push_back(Party(num, g));
      all_party++;
      all_num += num;
    }

    string ans = "";
    while(parties.size() > 0) {
      sort(parties.begin(), parties.end());
      if ( ans.size() > 0 ) { ans += " "; }
      if (parties.size() == 2 && parties[0].num == parties[1].num) {
	ans += parties[0].group + parties[1].group;
	parties[0].num--;
	parties[1].num--;
	if ( parties[0].num == 0 ) { break; }
      } else {
	ans += parties[0].group;
	parties[0].num--;
	if (parties[0].num == 0) {
	  parties.erase(parties.begin());
	}
      }
    }
    cout << "Case #" << t << ": " << ans << endl;
  }
}
