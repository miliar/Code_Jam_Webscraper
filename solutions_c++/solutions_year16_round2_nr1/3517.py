#include <bits/stdc++.h>

using namespace std;

const int maxn = 1e5 + 10;



int main()
{
	int T;
	cin >> T;
	int cas = 0;
	while (T--)
	{
		string s;
		int b[30];
		int res[10];
		cin >> s;
		memset(b, 0, sizeof(b));
		memset(res, 0, sizeof(res));
		int size = s.size();
		for (int i = 0; i < size; ++i)
		{
			b[s[i] - 'A']++;
		}
		int p = b['Z' - 'A'];
		res[0] += p;
		b['Z' - 'A'] -= p;
		b['E' - 'A'] -= p;
		b['R' - 'A'] -= p;
		b['O' - 'A'] -= p;
		p = b['W' - 'A'];
		res[2] += p;
		b['T' - 'A'] -= p;
		b['W' - 'A'] -= p;
		b['O' - 'A'] -= p;
		p = b['U' - 'A'];
		res[4] += p;
		b['F' - 'A'] -= p;
		b['O' - 'A'] -= p;
		b['U' - 'A'] -= p;
		b['R' - 'A'] -= p;
		p = b['X' - 'A'];
		res[6] += p;
		b['S' - 'A'] -= p;
		b['I' - 'A'] -= p;
		b['X' - 'A'] -= p;
		p = b['G' - 'A'];
		res[8] += p;
		b['E' - 'A'] -= p;
		b['I' - 'A'] -= p;
		b['G' - 'A'] -= p;
		b['H' - 'A'] -= p;
		b['T' - 'A'] -= p;
		p = b['O' - 'A'];
		res[1] += p;
		b['O' - 'A'] -= p;
		b['N' - 'A'] -= p;
		b['E' - 'A'] -= p;
		p = b['T' - 'A'];
		res[3] += p;
		b['T' - 'A'] -= p;
		b['H' - 'A'] -= p;
		b['R' - 'A'] -= p;
		b['E' - 'A'] -= p;
		b['E' - 'A'] -= p;
		p = b['F' - 'A'];
		res[5] += p;
		b['F' - 'A'] -= p;
		b['I' - 'A'] -= p;
		b['V' - 'A'] -= p;
		b['E' - 'A'] -= p;
		p = b['S' - 'A'];
		res[7] += p;
		b['S' - 'A'] -= p;
		b['E' - 'A'] -= p;
		b['V' - 'A'] -= p;
		b['E' - 'A'] -= p;
		b['N' - 'A'] -= p;
		p = b['I' - 'A'];
		res[9] += p;
		b['N' - 'A'] -= p;
		b['I' - 'A'] -= p;
		b['N' - 'A'] -= p;
		b['E' - 'A'] -= p;
		cout << "Case #" << ++cas << ": ";
		for (int i = 0; i < 10; ++i)
		{
			while (res[i])
			{
				cout << i;
				res[i]--;
			}
		}
		cout << endl;
	}


	return 0;
}