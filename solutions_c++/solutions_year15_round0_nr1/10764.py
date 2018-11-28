#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
  int testcases;
  cin >> testcases;
  for (int i = 0; i < testcases; ++i) {
    string shy_list;
    int max_shy;
    cin >> max_shy >> shy_list;
    vector<int> num_shy;
    for_each(shy_list.begin(), shy_list.end(), [&num_shy](const char& a) { num_shy.push_back(a - '0'); });
    int num_people = 0;
    int needed_people = 0;
    int shyness = 0;
    for (const auto& people : num_shy) {
      if (shyness != 0 && people != 0 && num_people < shyness) {
        needed_people += shyness - num_people;
        num_people += needed_people;
      }
      num_people += people;
      ++shyness;
    }
   cout << "Case #" << (i + 1) << ": " << needed_people << endl; 
  }
  return 0;
}
