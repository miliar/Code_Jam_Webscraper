#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<cstdlib>
using namespace std;

int main() {
  string line;
  getline(cin, line);
  int T = atoi(line.c_str());
  int S[1005];
  int Smax; 
  for(int i = 1; i <= T; ++i) {
    getline(cin, line);
    string delim = " ";
    int pos = line.find(delim);
    Smax = atoi(line.substr(0,pos).c_str());

    string rest = line.substr(pos+1);
    for(int j = 0; j <= Smax; ++j) {
      S[j] = rest[j] - '0';
    }
    int numPeople = 0;
    int neededPeople = 0;
    for(int j = 0; j <= Smax; ++j) {
      numPeople += S[j];
      if(numPeople <= j) {
	++neededPeople;
	++numPeople;
      }
    }
    cout << "Case #" << i << ": " << neededPeople << '\n';
  }
  return 0;
}
