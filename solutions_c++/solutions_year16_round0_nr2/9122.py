/*
ID: alperca1
LANG: C++
TASK: dualpal
*/

#include <bits/stdc++.h>

#ifdef NOT_UVA
#include <Windows.h>
#endif

using namespace std;

typedef unsigned long long ull;
typedef pair<ull, int> ulli;
typedef pair<int, int> ii;

#define INF (1<<30)

double pi = 3.14;

int resp[105],
resm[105];
string s;

int fm(int i);

int fp(int i)
{
	if (resp[i] != -1) return resp[i];

	if (i == 0)
	{
		if (s[0] == '-') return 1;
		else return 0;
	}

	if (s[i] == '+')
	{
		return resp[i] = fp(i - 1);
	}
	else
		return resp[i] = fm(i - 1) + 1;
}

int fm(int i)
{
	if (resm[i] != -1) return resm[i];

	if (i == 0)
	{
		if (s[0] == '+') return 1;
		else return 0;
	}

	if (s[i] == '-')
	{
		return resm[i] = fm(i - 1);
	}
	else
		return resm[i] = fp(i - 1) + 1;
}

int main(int argc, char **argv)
{
	//ios_base::sync_with_stdio(false);
#ifndef NOT_UVA
	//freopen("daireler.gir", "r", stdin);
	//freopen("daireler.cik", "w", stdout);
#endif
	
	int t;

	cin >> t;
	int cnt = 1;
	while (t--)
	{
	

		cin >> s;

		memset(resp, -1, sizeof resp);
		memset(resm, -1, sizeof resm);

		cout << "Case #" << cnt++ << ": " << fp(s.length() - 1) << endl;


	}

	end:
#ifdef NOT_UVA
	Sleep(-1);
#endif

	return 0;
}

