#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm> 
using namespace std;

int get_ind(char c) {
    return c - 'A';
}

void remove(vector<int>& char_counts, string s) {
  for (auto c: s) char_counts[get_ind(c)] --;
}

vector<int> extract_numbers(vector<int>& counts) {
  vector<pair<char, string> > pairs;
  pairs.push_back(make_pair('Z', "ZERO"));
  pairs.push_back(make_pair('W', "TWO"));
  pairs.push_back(make_pair('U', "FOUR"));
  pairs.push_back(make_pair('X', "SIX"));
  pairs.push_back(make_pair('G', "EIGHT"));
  pairs.push_back(make_pair('O', "ONE"));
  pairs.push_back(make_pair('R', "THREE"));
  pairs.push_back(make_pair('F', "FIVE"));
  pairs.push_back(make_pair('S', "SEVEN"));
  pairs.push_back(make_pair('N', "NINE"));
  vector<int> nums = {0,2,4,6,8,1,3,5,7,9};
  vector<int> res;
  for (int i = 0; i < nums.size(); i ++) {
      int n = nums[i];
      char c = pairs[i].first;
      string s = pairs[i].second;
      
      while (counts[get_ind(c)] > 0) {
	 res.push_back(n);
	 remove(counts, s);
      }	  
  }
  return res;
}

int main(int argc, char **argv) {
  std::string line;
  int T;
  cin >> T;
  std::getline(cin, line);
  for (int i = 0; i < T; i ++) {
    std::getline(cin, line);
    
    vector<int> char_counts(26, 0);
    for (auto c: line) {
      char_counts[get_ind(c)] ++;
    }
    
    vector<int> number = extract_numbers(char_counts);
    sort(number.begin(), number.end());
    
    cout << "Case #" << i + 1 << ": ";
    for (auto n: number) cout << n;
    cout << endl;
  }
}


