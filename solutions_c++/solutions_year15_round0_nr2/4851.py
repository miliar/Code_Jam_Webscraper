#include <bits/stdc++.h>
#define MAXN 1010

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        int P[MAXN], N, ANS = INT_MAX,rmax = -1;
        cin >> N;
        for (int i = 1; i <= N; i++)
		{
            cin >> P[i];
			rmax = max(rmax, P[i]);
	    }
        for (int i = 1; i <= rmax; i++)
        {
            int tot = 0;
            for (int j = 1; j <= N; j++)
            {
                int d = P[j]/i + ((P[j] % i == 0) ? 0 : 1);
                --d;
                tot += d;
            }
            ANS = min(ANS, tot + i);
        }
        cout << "Case #" << t << ": " << ANS << '\n';
    }
    return 0;
}
