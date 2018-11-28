#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <cstring>

using namespace std;

vector <int> u(105, 0) ,v(105, 0);
int T, N, M, o , e, p;

inline int O( int d )
{
	return (N*d - (d*(d-1))/2);
}

int main (int argc, char const* argv[])
{
	ifstream cin ("A-small.in");
	ofstream cout ("A-small.out");
	cin >> T;
	for (int t = 0; t < T; t += 1)
	{
		int ans = 0, org = 0, cost = 0;
		cin >> N >> M;
		for (int i = 0; i < M; i += 1)
		{
			cin >> o >> e >> p;
			u[o] += p;
			v[e] += p;
			org += p*O(e-o);
		}
		for (int i = 1; i <= N; i += 1)
		{
			int j = i;
			while ( v[i] != 0 )
			{
				if (v[i] > u[j])
				{
					cost += u[j]*(O(i-j));
					v[i] -= u[j];
					u[j] = 0;
				}
				else
				{
					cost += v[i]*(O(i-j));
					u[j] -= v[i];
					v[i] = 0;
				}
				j--;
			}
		}
		ans = org - cost;
		cout << "Case #" << t+1 << ": " << ans << '\n';
	}
	return 0;
}
