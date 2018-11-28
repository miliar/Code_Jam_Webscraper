#include <iostream>
#include <vector>

using namespace std;

int returnMults(vector<int>*& first, vector<int>*& second) {
  int result = 0;
  int dup = -1;
  for(int i = 0; i < 4; i++) {
    if (dup == -2) {
      break;
    }
    for(int j = 0; j < 4; j++) {
      if(first->at(i) == second->at(j)) {
 	result++;
	if(result == 1) {
	  dup = first->at(i);
	}
	else {
	  dup = -2; 
	}
	break;
      }
    }
  }
  return dup;
}

int main() {
  int cases;
  cin >> cases;
  for(int i = 0; i < cases; i++) {
    vector<vector<int>*>* first = new vector<vector<int>*>;
    vector<vector<int>*>* second = new vector<vector<int>*>;
    int row1, row2;
    cin >> row1;
    for(int j = 0; j < 4; j++) {
      vector<int>* row = new vector<int>;
      int a, b, c, d;
      cin >> a >> b >> c >> d;
      row->push_back(a);
      row->push_back(b);
      row->push_back(c);
      row->push_back(d);
      first->push_back(row);
    }
    cin >> row2;
    for(int j = 0; j < 4; j++) {
      vector<int>* row = new vector<int>;
      int a, b, c, d;
      cin >> a >> b >> c >> d;
      row->push_back(a);
      row->push_back(b);
      row->push_back(c);
      row->push_back(d);
      second->push_back(row);
    }
    vector<int>* onerow = first->at(row1 - 1);
    vector<int>* tworow = second->at(row2 - 1);
    int dups = returnMults(onerow, tworow);
    if (dups == -1) {
      cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
    }
    else if (dups == -2) {
      cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
    }
    else {
      cout << "Case #" << i+1 << ": " << dups << endl;
    }
  }
  return 0;
}
