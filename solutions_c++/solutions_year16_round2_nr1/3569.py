#include <iostream>
#include <string>
#include <string.h>
using namespace std;
typedef long long ll;

string Num[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

int a[26], rem, br=0;
int d[10];

int pos(int j)
{
	int b[26]; for (int i = 0; i < 26; i++) b[i] = a[i];
	for (int i = 0; i < Num[j].size(); i++) {
		b[Num[j][i]-'A']--;
		if (b[Num[j][i] - 'A' ] < 0)
			return 0;
	}
	return 1;
}
void recur()
{
	if (rem == 0)
	{
		for (int i = 0; i < 10; i++) for (int j = 0; j < d[i]; j++) cout << i;
		br = 1;
		return;
	}

	if (br == 0) 
	{
		for (int j = 0; j <= 9; j++)
		{
			if (pos(j))
			{
				rem -= Num[j].size(); d[j]++;
				for (int i = 0; i < Num[j].size(); i++)
					a[Num[j][i] - 'A']--;
				recur();
				rem += Num[j].size(); d[j]--;
				for (int i = 0; i < Num[j].size(); i++)
					a[Num[j][i] - 'A']++;

			}
		}
	}
	return;
}

int main()
{
	ios::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		memset(a, 0, sizeof(a));
		memset(d, 0, sizeof(d));
		br = 0;
		cout << "Case #" << t + 1 << ": ";
		string S; cin >> S; rem = S.size();
		for (int i = 0; i < S.size(); i++) a[S[i]-'A']++;
		recur();
		cout << endl;
	}
	return 0;
}
