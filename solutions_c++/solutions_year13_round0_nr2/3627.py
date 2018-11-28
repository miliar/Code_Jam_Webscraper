#include <iostream>
#include <cstdio>
using namespace std;
#define MAX2(a,b) (((a)>=(b))?(a):(b))

int main(int argc, char *argv[])
{
	freopen(argv[1], "r", stdin);
	freopen(argv[2], "w", stdout);

	int T;
	cin >> T;
	for (int t=0; t<T; t++)
	{
		int N, M;
		cin >> N >> M;
		int H[N][M];
		for (int n=0; n<N; n++)
			for (int m=0; m<M; m++)
				cin >> H[n][m];

		int maxR[N][M], maxL[N][M], maxD[N][M], maxU[N][M];
		for (int n=0; n<N; n++)
		{
			maxR[n][0] = H[n][0];
			for (int m=1; m<M; m++)
				maxR[n][m] = MAX2(maxR[n][m-1], H[n][m]);
			maxL[n][M-1] = H[n][M-1];
			for (int m=M-2; m>=0; m--)
				maxL[n][m] = MAX2(maxL[n][m+1], H[n][m]);
		}
		for (int m=0; m<M; m++)
		{
			maxD[0][m] = H[0][m];
			for (int n=1; n<N; n++)
				maxD[n][m] = MAX2(maxD[n-1][m], H[n][m]);
			maxU[N-1][m] = H[N-1][m];
			for (int n=N-2; n>=0; n--)
				maxU[n][m] = MAX2(maxU[n+1][m], H[n][m]);
		}


		bool possible = true;	bool debug[N][M];
		for (int n=0; n<N; n++)
		{
			for (int m=0; m<M; m++)
			{
				if (	(H[n][m] >= maxR[n][m] && H[n][m] >= maxL[n][m]) ||
					(H[n][m] >= maxD[n][m] && H[n][m] >= maxU[n][m]))
				{
					debug[n][m] = true;
					continue;
				}
				else
				{
					possible = false;
					debug[n][m] = false;
				}
			}
		}

		cout << "Case #" << t+1 << ": ";
		if (possible) cout << "YES" << endl;
		else cout << "NO" << endl;
/*
		for (int n=0; n<N; n++)
		{
			for (int m=0; m<M; m++)
			{
				cout << H[n][m] << " ";
			}
			cout << endl;
		}
		cout << "-----" << endl;
		for (int n=0; n<N; n++)
		{
			for (int m=0; m<M; m++)
			{
				if (n == 0 || m == 0 || n == N-1 || m == M-1)
					cout << "B ";
				else
					cout << debug[n][m] << " ";
			}
			cout << endl;
		}
		cout << "=================================" << endl;
*/
	}

	return 0;
}	



