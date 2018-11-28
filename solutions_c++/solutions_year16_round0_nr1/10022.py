#include <iostream>
#include <set>

using namespace std;

void addDigits(set<char> &digits, unsigned long long cnt)
{
	while (cnt > 0)
	{
		cerr << "insert " << (cnt % 10) << endl;
		digits.insert(cnt % 10);
		cnt /= 10;
	}
}

int main (int argc, char **argv)
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		set<char> digits;
		cout << "Case #" << i << ": ";
		unsigned long long N;
		cin >> N;
		unsigned long long cnt = 2*N;
		addDigits(digits, N);
		while ((digits.size() != 10) && (cnt != N))
		{
			cerr << "cnt: " << cnt << endl;
			addDigits(digits, cnt);
			cnt += N;
		}
		if (cnt == N) cout << "INSOMNIA";
		if (digits.size() == 10) cout << (cnt-N);
		cout << endl;
	}
}
