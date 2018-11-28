// B.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[])
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++){
	string s;
	cin >> s;
	int cnt = 0;
	reverse(s.begin(), s.end());
	char buff = '+';
	for (int j = 0; j < s.size(); j++){
	  if (s[j] != buff){
		buff = s[j];
		cnt++;
	  }
	}
	cout << "Case #" << i << ": " << cnt << endl;
  }
  return 0;
}

