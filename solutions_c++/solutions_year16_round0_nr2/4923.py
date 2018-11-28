#include <string.h>
#include <stdio.h>
#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

bool check(string s)
 {
  for(int i=0;i<s.size();i++) if(s[i]=='-') return false;
  return true;
 }
 
string flip(string s,  int p)
 {
  for(int i=0;i<=p;i++) if(s[i]=='-') s[i] = '+'; else s[i] = '-';
  //cout << p << ". " << s << endl;
  return s;
 }

int main()
 {
  int t,c;
  string s;
  cin >> t;
  for(int i = 0; i < t; i++)
   {
	cin >> s; c = 0;
	while(!check(s))
	 {
  	  for(int k = s.size(); k >= 0; k--) if(s[k] == '-') { s = flip(s,k); c++; }
	 }
	
    cout << "Case #" << i+1 << ": " << c << endl;
   }
  return 0;
 }
