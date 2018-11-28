
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T;	
	cin >> T;

  vector<vector<int> > B1(4, vector<int>(4));
  vector<vector<int> > B2(4, vector<int>(4));
  int R1;
  int R2;


  for(int t = 1; t <= T; t++) {

    cin >> R1;
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++) {
        cin >> B1[i][j];
      }

    cin >> R2;
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++) {
        cin >> B2[i][j];
      }

    R1--;
    R2--;

    sort(B1[R1].begin(), B1[R1].end());
    sort(B2[R2].begin(), B2[R2].end());

    vector<int> R;
    set_intersection(B1[R1].begin(), B1[R1].end(), B2[R2].begin(), B2[R2].end(), back_inserter(R));
    if(R.size() == 1) cout << "Case #" << t << ": " << R[0] << endl;
    else if(R.size() == 0) cout << "Case #" << t << ": " << "Volunteer cheated!" << endl;
    else cout << "Case #" << t << ": " << "Bad magician!" << endl;
  }


}
