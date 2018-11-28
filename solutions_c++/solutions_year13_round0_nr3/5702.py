#include <iostream>
#include <sstream>
#include <string>

using namespace std;

bool isPalindrome(long l)
{
	ostringstream ss;
	ss << l;
	string str = ss.str();

	int i = 0;
	int j = str.length() - 1;
	while (i < j) {
		if (str.at(i) != str.at(j))	return false;
		i++;
		j--;
	}
	return true;
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		long A, B;
		cin >> A >> B;

		int r = 0;
		for (int i = 1; i * i <= 1000; i++) {
			if (i * i < A)	continue;
			if (i * i > B)	break;

			if (isPalindrome(i) && isPalindrome(i*i)) {
				r++;
			}
		}

		cout << "Case #" << t << ": " << r << endl;
	}
}
