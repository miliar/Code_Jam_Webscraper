#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <sstream>
using namespace std;

fstream in, out;

int T;
int r1, r2;

vector<vector<int> > grid1(4);
vector<vector<int> > grid2(4);
set<int> nums;
set<int> ans_set;
string ans;

int main() {
  in.open("A-small-attempt0.in", fstream::in);
  out.open("proba-small.out", fstream::out);

  in >> T;
  for (int i = 0; i < T; i++) {
    in >> r1;
    for (int j = 0; j < 4; ++j) {
      grid1[j].clear();
      for (int k = 0; k < 4; ++k) {
	int temp;
	in >> temp;
	cout << temp << endl;
	grid1[j].push_back(temp);
      }
    }

    in >> r2;
    for (int j = 0; j < 4; ++j) {
      grid2[j].clear();
      for (int k = 0; k < 4; ++k) {
	int temp;
	in >> temp;
	cout << temp << endl;
	grid2[j].push_back(temp);
      }
    }
    
    nums.clear();
    for (int j = 0; j < 4; ++j) {
      nums.insert(grid1[r1 - 1][j]);
    }
    ans_set.clear();
    for (int j = 0; j < 4; ++j) {
      if (nums.count(grid2[r2-1][j]) > 0) {
	ans_set.insert(grid2[r2-1][j]);
      }
    }

    if (ans_set.size() == 1) {
      stringstream ss;
      ss << *ans_set.begin();
      ans = ss.str();
    } else if (ans_set.size() == 0) {
      ans = "Volunteer cheated!";
    } else {
      ans = "Bad magician!";
    }
    
    out << "Case #" << i + 1 << ": " << ans << endl;
  }
    
  in.close();
  out.close();
  return 0;
}
