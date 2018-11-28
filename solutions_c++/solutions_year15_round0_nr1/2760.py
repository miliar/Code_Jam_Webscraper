#include <bits/stdc++.h>

using namespace std;

long long T, S, N;
string P;

int main(int argc, char const *argv[])
{
	cin >> T;
	for (int tt = 0; tt < T; ++tt)
	{
		cin >> S;
		cin >> P;
		long long Si = 0, ans = 0;
		Si = (long long) (P[0] - '0');
		for (int i = 1; i <= S; ++i)
		{
			if ( i > Si )
			{
				ans += i - Si;
				Si = (long long)(P[i] - '0') + i;
			}
			else
			{
				Si += (long long)(P[i] - '0');
			}
		}
		cout << "Case #" << tt+1 << ": " << ans << '\n';
	}
	return 0;
}
