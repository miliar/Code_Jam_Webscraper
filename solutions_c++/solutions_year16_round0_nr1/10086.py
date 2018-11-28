#include <iostream>
#include <cstdio>
#include <string>
#include <random>
#include <vector>
#include <algorithm>

using namespace std;

FILE *istr;
FILE *ostr;

const int MASK = 0x3FF;

long long lastNumber(long long N) {
	int i = 1;
	int map = 0;
	while (i < 100) {
		long long num = N*i;
		while (num) {
			int digit = num % 10;
			map = map | (1 << digit);
			num = num / 10;
		}
		if ((map ^ MASK) == 0) {
			return N*i;
		}			
		i++;
	}

	return -1;
}

//vector<string> arr;
void main()
{
	freopen_s(&istr, "A-large.in", "r", stdin);
	freopen_s(&ostr, "A-large.out", "w", stdout);

	int t;
	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		int n;
		cin >> n;
		long long ans = lastNumber(n);
		// tried for 10000 times and not found
		if (ans == -1)
		{
			cout << "Case #" << i << ": ";
			cout << "INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << i << ": ";
			cout << ans << endl;
		}

	}
	//system("pause");

}