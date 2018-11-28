#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main () {
  string x;
  getline(cin, x);
  int t = stoi(x);


  for (int a = 0; a < t; a++) {
    string s;
    getline(cin, s);

    vector<bool> pancakes;
    int last_unhappy = -1;

    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '+')
        pancakes.push_back(true);
      else {
        pancakes.push_back(false);
      }
    }


    int flips = 0;
    while (true) {
      int curindex = 0;
      while (curindex < s.size() && pancakes[curindex] == pancakes[0])
        curindex++;

      if (curindex == s.size()) break;

      int start = 0;
      int end = curindex - 1;
      while (start < end) {
        swap(pancakes[start], pancakes[end]);
        start++;
        end--; 
      }
      
      for (int i = 0; i < curindex; i++)
        pancakes[i] = !pancakes[i];

      flips++;
    }

    if (pancakes[0] == false)
      flips++;

      cout << "Case #" << (a+1) << ": " << flips << endl;
  }

}