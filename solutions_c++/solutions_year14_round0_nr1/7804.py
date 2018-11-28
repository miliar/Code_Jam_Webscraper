#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int fa[4][4];
int sa[4][4];

int main() {
  int T=0; cin >> T;
  for (int t = 0; t < T; ++t) {
    // reading input for case T
    int fc=0, sc=0;
    cin >> fc;
    fc--;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
	cin >> fa[i][j];
      }
    }
    cin >> sc;
    sc--;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
	cin >> sa[i][j];
      }
    }
    // filtering values by first answer
    vector<int> vfa;
    for (int i = 0; i < 4; ++i) {
      vfa.push_back(fa[fc][i]);
      //cout << "vfa " << vfa[i] << endl;
    }
    // filtering values by second answer
    vector<int> vsa;
    for (int i = 0; i < 4; ++i) {
      vsa.push_back(sa[sc][i]);
      //cout << "vsa " << vsa[i] << endl;
    }
    // final result
    sort(vfa.begin(), vfa.end());
    sort(vsa.begin(), vsa.end());
    vector<int> r(8, 0);
    vector<int>::iterator ite;
    ite = set_intersection(vfa.begin(), vfa.end(), 
			   vsa.begin(), vsa.end(), 
			   r.begin());

    r.resize(ite-r.begin());
    // printing intersection
    if (r.size() == 1)
      cout << "Case #" << t+1 << ": " << r[0] << endl;
    if (r.size() > 1)
      cout << "Case #" << t+1 << ": Bad magician!" << endl;
    if (r.size() == 0)
      cout << "Case #" << t+1 << ": Volunteer cheated!" << endl;
  }

  return 0;
}
