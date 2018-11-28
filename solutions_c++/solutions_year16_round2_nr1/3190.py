#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

vector<string> num;
map<char, int> chars;
vector<int> sol;

void init() {
  num = vector<string>();
  num.push_back("ZERO");
  num.push_back("ONE");
  num.push_back("TWO");
  num.push_back("THREE");
  num.push_back("FOUR");
  num.push_back("FIVE");
  num.push_back("SIX");
  num.push_back("SEVEN");
  num.push_back("EIGHT");
  num.push_back("NINE");
}

int getNChar(char c) {
  map<char, int>::iterator it = chars.find(c);
  if (it == chars.end()) {
    return 0;
  }
  return it->second;
}


void discount(int n, int times) {
  // cout << "discount " << n << " " << times << endl;
  string s = num[n];
  map<char, int>::iterator it;
  for (int i = 0; i < s.size(); ++i) {
    it = chars.find(s[i]);

    //cout <<"ad" << endl;
    //cout << it->first << endl;
    it->second = it->second - times;
  }
}

void determineBasedOnChar(int n, char c) {
  //cout << "d" << endl;
  int count = getNChar(c);
  sol[n] = count;
  // cout << "solution " << n << " = " << sol[n] << endl;
  discount(n, sol[n]);
}

int main(int argc, char** argv) {
  init();
  int T;
  cin >> T;
  int t = 0;
  for (int t = 1; t <= T; ++t) {
    string s;
    cin >> s;
    // cout << s << endl;

    chars = map<char, int>();
    map<char, int>::iterator it;
    for (int i = 0; i < s.size(); ++i) {
      char c = s[i];
      it = chars.find(c);
      if(it == chars.end()) {
        chars.insert(pair<char, int>(c, 1));
      } else {
        it->second++;
      }
    }

/*
    cout << "count" << endl;
    it = chars.begin();
    while(it != chars.end()) {
      cout << it->first << " " << it->second << endl;
      it++;
    }
    */


    sol = vector<int> (10, 0);
    determineBasedOnChar(0, 'Z');
    determineBasedOnChar(2, 'W');
    determineBasedOnChar(6, 'X');
    determineBasedOnChar(8, 'G');
    determineBasedOnChar(3, 'H');
    determineBasedOnChar(4, 'U');
    determineBasedOnChar(5, 'F');
    determineBasedOnChar(7, 'V');
    determineBasedOnChar(1, 'O');
    determineBasedOnChar(9, 'I');

    stringstream ss;


    /*
    cout << "SOLUTION" << endl;
    for (int i = 0; i < sol.size(); ++i) {
      cout << sol[i] << " ";
    }
    cout << "" << endl;
    */

    for (int i = 0; i < 10; ++i) {
      for (int j = 0; j < sol[i]; ++j) ss << i;
    }

    string solS;
    ss >> solS;

    cout << "Case #" << t << ": " << solS << endl;
  }
  return 0;
}
