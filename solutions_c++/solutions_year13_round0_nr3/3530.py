#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

bool check (long long a)
{
	vector <int> num;
	while (a)
	{
		num.push_back (a % 10);
		a /= 10;
	}
	for (int i = 0; i < num.size ()/2; ++i)
		if (num [i] != num [num.size () - i - 1])
			return false;
	return true;
}

int main ()
{
	ifstream cin ( "input.txt" );
	ofstream cout ( "output.txt" );
	int t;
	cin >> t;
	int all = t;
	while (t--)
	{
		bool flag = false;
		cout << "Case #" << all-t << ": ";
		long long l, r;
		cin >> l >> r;
		vector <long long> palindromes;
		for (long long i = 1; i * i <= r; ++i)
			if (i * i >= l && check (i))
				palindromes.push_back (i);
		long long ans = 0;
		for (int i = 0; i < palindromes.size (); ++i)
			if (check (palindromes [i] * palindromes [i]))
				++ans;
		cout << ans << endl;
	}
}