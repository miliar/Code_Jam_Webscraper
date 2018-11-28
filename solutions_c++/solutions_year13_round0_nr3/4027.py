#include <iostream>
#include <set>
using namespace std;
#include "BigIntegerLibrary.hh"

set<BigInteger> all;

bool isPalindrome(BigInteger& i)
{
	string s = bigIntegerToString(i);
	int count = (int)s.length() / 2;
	for (int i = 0; i < count; i++)
	{
		if (s[i] != s[s.length() - i - 1]) return false;
	}
	return true;
}

void process(int t)
{
	string s;
	cin >> s; BigInteger a = stringToBigInteger(s);
	cin >> s; BigInteger b = stringToBigInteger(s);

	int count = 0;
	for (set<BigInteger>::iterator it = all.begin(); it != all.end(); it++)
	{
		BigInteger i = *it;
		if (a <= i && i <= b) count++;
	}
	cout << "Case #" << t << ": " << count << endl; // gilgil temp
}

void getAll()
{
	string s("100000000000000"); //10^14
	BigInteger max = stringToBigInteger(s);
	for (BigInteger root = 1; true; root++)
	{
		BigInteger square = root * root;
		if (square > max) break;
		if (isPalindrome(root) && isPalindrome(square))
		{
			all.insert(square);
		}
	}
	// cout << all.size() << endl; // gilgil temp
	// for (set<BigInteger>::iterator it = all.begin(); it != all.end(); it++) cout << *it << endl; // gilgil temp
}
int main()
{
	getAll();
	int T; cin >> T;
	for (int t = 1; t <= T; t++)
		process(t);
	return 0;
}