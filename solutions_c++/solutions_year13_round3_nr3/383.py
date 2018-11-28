#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<cmath>
#include<algorithm>
#include<queue>

using namespace std;

//long long h[200001000];
long long h[2000100];
//const int D = 100000200;
const int D = 1000020;
const int b_size = 14000;

int d[1100], d_d[1100], n[1100], w[1100], e[1100], s[1100], d_p[1100], d_s[1100];

void main(){
#ifdef MY_TEST_VAR
   freopen("input.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif
//memset(h, 0, sizeof(h));
	int T;
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		memset(h, 0, sizeof(h));
		int N;
		scanf("%d", &N);
		int ans = 0;
		for (int i = 0; i < N; i++)
		{
			scanf("%d%d%d%d%d%d%d%d\n", d + i, n + i, w + i, e + i, s + i, d_d + i, d_p + i, d_s + i);
		}

		for (int time = 0; time < 700000; time++)
		{
			for (int i = 0; i < N; i++)
				if (time >= d[i] && (time - d[i]) % d_d[i] == 0)
				{
					int tr = (time - d[i]) / d_d[i];
					if (tr >= n[i]) continue;
					long long m = 200000100;
					int l = w[i] + tr * d_p[i];
					int r = e[i] + tr * d_p[i];
					int t_s = s[i] + tr * d_s[i];
					for (int j = l; j < r; j++)
						if (m > h[j + D])
							m = h[j + D];
					if (m < t_s)
					{
						ans++;
					//printf("Day %d, Tribe %d\n", time, i);
					}
	/*										for (int i = 0; i < 20; i++)
						printf("%lld ", h[i + D]);
					printf("\n");*/
			
				}
			for (int i = 0; i < N; i++)
				if (time >= d[i] && (time - d[i]) % d_d[i] == 0)
				{
					int tr = (time - d[i]) / d_d[i];
					if (tr >= n[i]) continue;
					int l = w[i] + tr * d_p[i];
					int r = e[i] + tr * d_p[i];
					int t_s = s[i] + tr * d_s[i];
					for (int j = l; j < r; j++)
						if (t_s > h[j + D])
							h[j + D] = t_s;
				}
		}
		printf("Case #%d: %d\n", I, ans);
	}
}