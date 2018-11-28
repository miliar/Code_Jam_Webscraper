#include <bits/stdc++.h>

using namespace std;

long long T, S, N, D, pancakes, cuts;
deque< long long > P;

int main(int argc, char const *argv[])
{
	cin >> T;
	for (int tt = 0; tt < T; ++tt)
	{
		cin >> D;
		P.clear();
		long long mcut = 0;
		for (int i = 0; i < D; ++i)
		{
			cin >> pancakes;
			P.push_back(pancakes);
			mcut = max(mcut, pancakes);
		}
		long long ans = mcut;
		cuts = 0;
		for (int i = 1; i < 1009; ++i)
		{
			cuts = 0;
			for (int j = 0; j < P.size(); ++j)
			{
				cuts += (P[j]/i);
				if( P[j] % i == 0 )
                    cuts--;
			}
			ans = min(ans, cuts+i);
		}
		cout << "Case #" << tt+1 << ": " << ans << '\n';
	}
	return 0;
}
