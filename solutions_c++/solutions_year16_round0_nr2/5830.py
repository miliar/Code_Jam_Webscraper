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

bool check(string str)
 {
  for(int i=0;i<str.size();i++) if(str[i]=='-') return false;
  return true;
 }
 
string flip(string str,  int num)
 {
  for(int i=0;i<=num;i++) if(str[i]=='-') str[i] = '+'; else str[i] = '-';
   
  return str;
 }

int main()
 {
  int t,c;
  string str;
  cin >> t;
  for(int i = 0; i < t; i++)
   {
	cin >> str; c = 0;
	while(!check(str))
	 {
  	  for(int k = str.size(); k >= 0; k--) if(str[k] == '-') { str = flip(str,k); c++; }
	 }
	
   
   
   
    cout << "Case #" << i+1 << ": " << c << endl;
   }
  return 0;
 }
