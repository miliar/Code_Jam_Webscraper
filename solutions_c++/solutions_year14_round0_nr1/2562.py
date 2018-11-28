#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <iostream>
#include <iterator>

using namespace std;

int main()
{
  int T;
  cin >> T;

  for (int cs = 1; cs <= T; ++cs) {
    int a1, a2;
    vector<vector<int> > g1(4, vector<int>(4));
    vector<vector<int> > g2(4, vector<int>(4));
    vector<int> intersect;

    cin >> a1;
    --a1;
    for (int r = 0; r < 4; ++r) for (int c = 0; c < 4; ++c) cin >> g1[r][c];
    sort(g1[a1].begin(), g1[a1].end());

    cin >> a2;
    --a2;
    for (int r = 0; r < 4; ++r) for (int c = 0; c < 4; ++c) cin >> g2[r][c];
    sort(g2[a2].begin(), g2[a2].end());

    set_intersection(g1[a1].begin(), g1[a1].end(),
		     g2[a2].begin(), g2[a2].end(),
		     inserter(intersect, intersect.begin()));
    
    cout << "Case #" << cs << ": ";

    switch (intersect.size()) {
    case 0:
      cout << "Volunteer cheated!" << endl;
      break;
    case 1:
      cout << *intersect.begin() << endl;
      break;
    default:
      cout << "Bad magician!" << endl;
      break;
    }
    
  }

  return 0;
}
