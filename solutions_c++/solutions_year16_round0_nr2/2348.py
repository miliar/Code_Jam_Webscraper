//============================================================================
// Name        : pancakes.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>

int solve(const std::string& s)
{
  int n = s.length();
  if(n==0)
    return 0;
  int k=1;
  for(int i=1; i<n; i++)
    if(s[i-1] != s[i])
      k++;
  if(s[n-1] == '+')
    k--;
  return k;
}
int main() {
	int t;
	std::cin >> t;
	std::string s2;
	getline(std::cin, s2);
	for(int i=0; i<t; i++)
	{
		std::string s;
		getline(std::cin, s);
		std::cout << "Case #" << i+1 << ": " << solve(s)<<std::endl;
	}

	return 0;
}
