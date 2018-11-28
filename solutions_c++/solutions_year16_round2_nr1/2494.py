#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;


int main () {
  vector<string> letters = {"ZERO", "XIS", "SEVEN", "GEIHT", "UFOR", "HRTEE", "FVIE", "TWO", "INNE", "ONE"};
  vector<int> values = {0, 6, 7, 8, 4, 3, 5, 2, 9, 1};
  long long q;
  cin >> q;
  string input;
  for (int i = 0; i < q; i++) {
    cin >> input;
    string output;
    map<char, int> digs;
    for (int j = 0; j < input.size(); j++) {
      digs[input[j]] ++;
    }
    for (int j = 0; j < 10; j++) {
      //is the number in the map?
      bool isInMap = false;
      for (int k = 0; k < letters[j].size(); k++) {
// 	cout << "checking for " << letters[j][k] << endl;
	if (digs.count(letters[j][k]) > 0 && digs[letters[j][k]] != 0) {
// 	  cout << "found " << letters[j][k] << endl;
	  digs[letters[j][k]]--;
	  isInMap = true;
	} else {
	  //should break on the first letter
	  isInMap = false;
	  break;
	}
      }
      if (isInMap) {
	output += (to_string(values[j]));
// 	cout << "FOUND " << values[j] << endl;
	j--;
      } else {
// 	cout << "DIDN'T FIND " << values[j] << endl;
      }
    }
    sort(output.begin(), output.end());
    cout << "Case #" << i+1 << ": " << output << endl;
  }
  return 0;
}