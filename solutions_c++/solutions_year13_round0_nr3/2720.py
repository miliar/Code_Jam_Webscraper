//Google Codejam
//2013 Qualification Round
//Alan Richards - alarobric

//Problem C
#include <sstream>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <cmath>
#include <algorithm>
using namespace std;

#define FOR(i, n) for(int i=0; i<n; i++)
#define FOREACH(c, iter) for(auto iter=c.begin(); iter!=c.end(); iter++)

vector<int> arrM;

bool isPalindrome(int i)
{
	std::stringstream ss;
	ss << i;
	string s = ss.str();
	std::reverse(s.begin(), s.end());
	if (ss.str() == s)
		return true;
	return false;
}

int Solve(int i_case)
{
	int A, B;
	std::cin >> A >> B;
	int a = floor(sqrt(A));
	int b = ceil(sqrt(B));
	
	//for a…b, if a is a palindrome, check if a*a is a palindrome, then count it
	int numFairSquare = 0;
	for (int i=a; i<=b; i++)
	{
		if (isPalindrome(i) && isPalindrome(i*i) && i*i <= B && i*i >= A)
			numFairSquare++;
	}
	
	return numFairSquare;
}

int main()
{
	std::cerr << "GCJ Practice" << std::endl;
	int numCases;
	std::cin >> numCases;
	for (int i=1; i<=numCases; i++)
	{
		std::cout << "Case #" << i << ": " << Solve(i) << std::endl;
	}
	return 0;
}