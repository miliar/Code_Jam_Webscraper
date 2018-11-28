#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <fstream>
#include <map>
#include <cstring>
using namespace std;

int allPlus(string s) {
  for(int i=0;i<s.size();i++) {
    if(s[i] != '+')return 0;
  }
  return 1;
}

int main() { 
  ofstream output;
  output.open("output.txt");
  int t;
  cin >> t;
  for(int i=1;i<=t;i++) {
    string s;
    cin >> s;
    char ch;
    int p,count=0;
    while(allPlus(s)!=1) {
      count = count +1;
      //cout<<s<<endl;
      ch = s[0];
      p = 0;
      while(p < s.size()) {
	p = p + 1;
	if(s[p] == ch) continue;
	else break;
      }
      for(int l = 0; l < p; l++) {
	if(ch == '-') s[l] = '+';
	else s[l] = '-';
      }
    }
    output << "Case #" << i << ": "<<count<<endl;
  } 
  return 0; 
}
