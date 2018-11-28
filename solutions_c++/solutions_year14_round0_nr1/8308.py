#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  size_t ntests;
  cin >> ntests;

  for(size_t i=0 ; i< ntests ; i++) {
    vector< vector< int > > data1, data2;
    size_t row1, row2;
    cin >> row1;
    // Fix indexing
    row1--;
    for(int j = 0 ; j < 4 ; j++) {
      vector<int> row;
      for(int k = 0 ; k < 4 ; k++) {
	int num;
	cin >> num;
	row.push_back(num);
      }
      data1.push_back(row);
    }
    cin >> row2;
    // fix index number
    row2--;
    for(int j = 0 ; j < 4 ; j++) {
      vector<int> row;
      for(int k = 0 ; k < 4 ; k++) {
	int num;
	cin >> num;
	row.push_back(num);
      }
      data2.push_back(row);
    }

    vector<int> intersect;
    
    sort(data1[row1].begin(), data1[row1].end());
    sort(data2[row2].begin(), data2[row2].end());

    set_intersection(data1[row1].begin(), data1[row1].end(),
		     data2[row2].begin(), data2[row2].end(),
		     back_inserter(intersect));

    cout << "Case #" << i+1 <<": ";
    if(intersect.size() == 0) {
      cout << "Volunteer cheated!" << endl;
    } else if(intersect.size() == 1) {
      cout << intersect[0] << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }
}
