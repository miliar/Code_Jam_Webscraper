#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <set>
#include <string>
#include <iomanip>
 
using namespace std;
 
int number(string &s, int n, bool reverse)
{
	for (int i = n; i >= 0; i--) {
		if ((s[i] == '-') == reverse)
			continue;
		return 1 + number(s, i, !reverse);
	}
	return 0;
}

int main()
{

	int T;

	cin >> T;

	for (int i = 0; i < T; i++) {

		string s;

		cin >> s;
		
      cout << "Case #" << i+1 << ": ";
		cout << number(s, s.length()-1, false) << endl;

	}

	return 0;
}

