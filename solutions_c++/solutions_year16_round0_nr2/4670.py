#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int T;

int solve(string str)
{
	int a = 0;
	int i=str.size()-1;
	while (i>=0 && str[i] == '+') --i;
	if (i == -1) return 0;

	if (str[0] == '+') a=1;

	for (int j=0; j<=i && str[j] == '+'; ++j) {
		str[j] = '-';
	}

	string n;
	for (int j = i; j>=0; --j) {
		n.append( 1, (str[j] == '+')? '-': '+');
	}
	return solve(n)+a+1;
}

int main()
{
	cin >> T;
	for (int t=1; t<=T; ++t) {
		string str;
		cin >> str;
		cout << "Case #" << t << ": " << solve(str) << endl;
	}
}