
#include <iostream>
#include <string>

using namespace std;

const char * numbers[10] = 
{
	"ZERO",
	"ONE",
	"TWO",
	"THREE",
	"FOUR",
	"FIVE",
	"SIX",
	"SEVEN",
	"EIGHT",
	"NINE",
};

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		string s;
		cin >> s;

		int occur[256];
		memset(occur, 0, sizeof(occur));
		for (unsigned int k = 0; k < s.length(); ++k)
		{
			char c = s[k];
			occur[c] += 1;
		}
		int number[10];
		memset(number, 0, sizeof(number));

		int alloccur = 0;
		int z = occur['Z'];
		alloccur += z;
		if (z)
		{
			number[0] += z;
			occur['Z'] -= z;
			occur['E'] -= z;
			occur['R'] -= z;
			occur['O'] -= z;
		}

		int w = occur['W'];
		alloccur += w;
		if (w)
		{
			number[2] += w;
			occur['T'] -= w;
			occur['W'] -= w;
			occur['O'] -= w;
		}

		int x = occur['X'];
		alloccur += x;
		if (x)
		{
			number[6] += x;
			occur['S'] -= x;
			occur['I'] -= x;
			occur['X'] -= x;
		}

		int g = occur['G'];
		alloccur += g;
		if (g)
		{
			number[8] += g;
			occur['E'] -= g;
			occur['I'] -= g;
			occur['G'] -= g;
			occur['H'] -= g;
			occur['T'] -= g;
		}

		int u = occur['U'];
		alloccur += u;
		if (u)
		{
			number[4] += u;
			occur['F'] -= u;
			occur['O'] -= u;
			occur['U'] -= u;
			occur['R'] -= u;
		}

		int f = occur['F'];
		alloccur += f;
		if (f)
		{
			number[5] += f;
			occur['F'] -= f;
			occur['I'] -= f;
			occur['V'] -= f;
			occur['E'] -= f;
		}

		int h = occur['H'];
		alloccur += h;
		if (h)
		{
			number[3] += h;
			occur['T'] -= h;
			occur['H'] -= h;
			occur['R'] -= h;
			occur['E'] -= h;
			occur['E'] -= h;
		}

		int v = occur['V'];
		alloccur += v;
		if (v)
		{
			number[7] += v;
			occur['S'] -= v;
			occur['E'] -= v;
			occur['V'] -= v;
			occur['E'] -= v;
			occur['N'] -= v;
		}

		int ii = occur['I'];
		alloccur += ii;
		if (ii)
		{
			number[9] += ii;
			occur['N'] -= ii;
			occur['I'] -= ii;
			occur['N'] -= ii;
			occur['E'] -= ii;
		}

		int e = occur['E'];
		alloccur += e;
		if (e)
		{
			number[1] += e;
			occur['O'] -= e;
			occur['N'] -= e;
			occur['E'] -= e;
		}


		int ans = 66;
		cout << "Case #" << i << ": ";
		for (int k = 0; k < 10; ++k)
		{
			for (int x = 0; x < number[k]; ++x)
				cout << k;
		}
		cout << endl;
	}

	return 0;
}
