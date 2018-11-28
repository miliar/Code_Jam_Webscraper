#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int stoi(char s) {
  
  return s - '0';
}
int main() {
  ifstream f;
  f.open("A-large.in");
  string curr;
  getline(f, curr);
  istringstream iss(curr);
  int cases;
  iss >> cases;
  for(int c=1;c<=cases;++c) {
    getline(f, curr);
    istringstream iss(curr);
    int garb;
    iss >> garb;
    string list;
    iss >> list;
    int * csum = new int[list.length()];
    for (int k=0;k<list.length();++k) csum[k] = 0;

    csum[0] = stoi(list[0]);
    //cout << "csum " << csum[0];
    for (int s=1;s<list.length();++s) {
      csum[s] = csum[s-1] + stoi(list[s]);
    //  cout << " " << csum[s];
    }
    //cout << endl;

    int max = 0;
    for (int s=1;s<list.length();++s) {
      int curr = s;
      if (csum[s-1] < s) {
        if (max < s - csum[s-1]) {
          max = s - csum[s-1];
        }
      }
    }

    cout << "Case #" << c << ": " << max << endl;
  }
}
