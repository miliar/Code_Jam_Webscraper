#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using std::cin;  using std::cout;  using std::endl;
using std::vector; using std::string;

int main() {

  int T;
  cin >> T;

  for (int i=1; i<=T; ++i) {

    int N;
    cin >> N;

    /*
    vector<vector<int> > lists(2*N-1);
    for (int j = 0; j< 2*N-1;  ++j) {
      lists[j] = vector<int>(N);
      for (int k = 0; k< N;  ++k) {
	cin >> lists[j][k];
      }
    }
    */

    int soldier;
    vector<int> soldiers(2501);
    for (int j = 0; j< 2*N-1;  ++j) {
      for (int k = 0; k< N;  ++k) {
	cin >> soldier;
	++ soldiers[soldier];
      }
    }

    cout << "case #" << i << ":";
    for (int j = 1; j< 2501;  ++j) {
      if (soldiers[j] != 0
	  && soldiers[j] % 2 == 1) {
	cout << " " << j;
      }
    }
    cout << endl;
    /*
    sort(lists.begin(), lists.end());

    for (int j = 0; j< 2*N-1;  ++j) {
      for (int k = 0; k< N;  ++k) {
	cout << lists[j][k] << " ";
      }
      cout << endl;
    }
    */
    
    /*
    sorted = sorted + letters[0];
    for (int j = 1; j< letters.length();  ++j) {
      if (letters[j] >= sorted[0])
	sorted = letters[j] + sorted;
      else
	sorted = sorted + letters[j];
    }
    cout << "case #" << i << ": " << sorted << endl;
    */
  }

  return 0;
}
