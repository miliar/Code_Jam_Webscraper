/*Krypto...........................jagsxi..........!!! */
/*Google Code Jam Round1B */
#include<bits/stdc++.h>
using namespace std;
#define MAX 1111111
int DP[MAX];

int rev(int x)
{
	int y = 0;
	while (x > 0)
	{
		y = y * 10 + (x % 10);
		x /= 10;
	}
	return y;
}

queue<int> Q;
int main()
{

  freopen("1.txt", "r", stdin);
  freopen("1o.txt", "w", stdout);
	DP[1] = 1;
	Q.push(1);
	while (!Q.empty())
	{
		int x = Q.front();
		Q.pop();
		if (x + 1 < MAX and DP[x + 1] == 0)
		{
			DP[x + 1] = DP[x] + 1;
			Q.push(x + 1);
		}
		if (rev(x) < MAX and DP[rev(x)] == 0)
		{
			DP[rev(x)] = DP[x] + 1;
			Q.push(rev(x));
		}
	}
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		long long N;
		cin >> N;	
		printf("Case #%d: %d\n", t, DP[N]);
	}
}