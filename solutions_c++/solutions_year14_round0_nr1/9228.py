#include <iostream>
#include <set>

using namespace std;

int main() {

  int TC;
  int input;
  int arr[4][4];

  cin >> TC;

  for (int tc = 1; tc <= TC; tc++) {
    set<int> myset;
    set<int>::iterator it;
    int answer;
    int cnt = 0;
    
    cin >> input;

    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
	cin >> arr[i][j];
	if (input == i+1) myset.insert(arr[i][j]);
      }
    }

    cin >> input;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
	cin >> arr[i][j];
	if (input == i+1) {
	  it = myset.find(arr[i][j]);
	  if (it != myset.end()) {
	    answer = arr[i][j];
	    cnt++;
	  }
	}
      }
    }

    if(cnt == 1) {
      cout << "Case #" << tc << ": " << answer << endl;
    } else if (cnt == 0) {
      cout << "Case #" << tc << ": Volunteer cheated!" << endl;
    } else {
      cout << "Case #" << tc << ": Bad magician!" << endl;
    }

    myset.clear();
  }
  return 0;
}
