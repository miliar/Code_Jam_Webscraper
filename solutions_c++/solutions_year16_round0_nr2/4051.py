#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int t;

int cal(string s) {
  int cnt = 0;
  int str[100];

  for(int i = 0; i < s.length(); i++) {
    if(s.at(i) == '+') 
      str[i] = 1;
    else
      str[i] = 0;
  }

  int before = 0;
  for(int i = 0; i < s.length(); i++) {
    if(str[i] != before) {
      if(i != 0) {
        cnt += 1;
      }
      before = str[i];
    }

    if(i == s.length() - 1) {
      if(before == 0) cnt += 1;
    }
  }

  return cnt;
}

int main() {
  //ifstream in("in.txt");
  //ifstream in("B-small-attempt0.in");
  ifstream in("B-large.in");
  ofstream out("out.txt");
  in >> t;

  string s;
  for(int i = 0; i < t; i++) {
    in >> s;
    out << "Case #" << i + 1 << ": " << cal(s) << endl;
  }
}
