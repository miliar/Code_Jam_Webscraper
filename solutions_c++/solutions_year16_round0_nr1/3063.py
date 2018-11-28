#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for(i = (a) ; i<(b) ; i++)
#define RFOR(i, a, b) for(i = (a)-1 ; i>=(b); i--)
#define MEM(a,b) memset(a,b,sizeof(a))

//#define SMALL 1
#define SMALL 0

bool digitArr[10];
void Solve()
{
	long long N;
	int i, j;
	int digit;

	long long name;
	long long result;
	bool IsSleep;

	cin >> N;
	if (N == 0) {
		cout << "INSOMNIA" << endl;
		return;
	}
	i = 1;
	IsSleep = false;
	memset(digitArr, false, sizeof(digitArr));
	while (IsSleep == false)
	{
		name = N * (i++);
		result = name;
		while (name != 0)
		{
			digit = name % 10;
			if (digitArr[digit] == false)
				digitArr[digit] = true;
			name = name / 10;
		}

		FOR(j, 0, 10)
		{
			if (digitArr[j] == false)
				break;
			else if (j == 9)
				IsSleep = true;
		}
	}
	cout << result << endl;
}

int main()
{
	if (SMALL)
	{
		freopen("A-small-attempt0.in", "r", stdin);
		freopen("A-small-attempt0.out", "w", stdout);
	}
	else
	{
		freopen("A-large.in", "r", stdin);
		freopen("A-large.out", "w", stdout);
	}

	int t, T;
	cin >> T;
	FOR(t, 0, T)
	{
		cout << "Case #" << t + 1 << ": ";
		Solve();
	}

	return 0;
}