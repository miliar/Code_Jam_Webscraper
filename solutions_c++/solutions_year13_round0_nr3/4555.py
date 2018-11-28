#include <iostream>
#include <cmath>
#include <sstream>

using namespace std;

#define UI unsigned long long

bool isPalindrome(UI x)
{
	// Convert to characters
	ostringstream os;
	os << x;
	string s = os.str();

	// detect palindrome
	for(unsigned int i = 0; i < s.length(); ++i)
	{
		if(s.at(i) != s.at(s.length() - 1 - i))
			return false;
	}

	return true;
}

UI process(UI A, UI B)
{
	UI count = 0;

	// get roots

	UI min_root = (UI)sqrt((long double)A);
	UI max_root = (UI)sqrt((long double)B);

	if((min_root * min_root) < A)
		++min_root;
	
	if((max_root * max_root) > B)
		--max_root;

	for(UI root = min_root; root <= max_root; ++root)
	{
		// is root and square of root a palindrome?
		if(isPalindrome(root) && isPalindrome(root * root))
		{
			++count;
		}
	}

	return count;
}

void main()
{
	UI T, A, B, result;

	cin >> T;

	for(int t = 0; t < T; ++t)
	{
		cout << "Case #" << t+1 << ": ";
		
		cin >> A >> B;
		result = process(A, B);
		cout << result << endl;
	}
}