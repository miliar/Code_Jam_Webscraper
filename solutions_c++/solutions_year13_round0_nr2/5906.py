#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <complex>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>
#include <ctime>

const double pi = 3.1415926535897932384626433832795;
const int INF = 2000000000;
double E=1e-9;

#define sz size()
#define pb push_back
#define ALL(a) (a).begin(), (a).end()
#define MEMS(a,b) memset(a,b,sizeof(a))
#define sqr(a) ((a)*(a))
#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)
#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define VVI vector < vector <int> >
#define VI vector <int>
#define LL long long
LL gcd(LL a, LL b){if (a==0) return b;return gcd(b%a,a);}
LL lcm (LL a, LL b) {return a / gcd (a, b) * b;}

using namespace std;

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
		
	FOR(q, 0, T)
	{
		int N, M, max = 0;
		string maxStr = "";
		cin >> N >> M;
		VVI in(N), cur(N);

		FOR(i, 0, N)
			FOR(j, 0, M){
				int x;
				cin >> x;
				in[i].pb(x);
				max = MAX(max, x);
			}
		
		FOR(i, 0, N)
			FOR(j, 0, M)
				cur[i].pb(max);

		if(N == 1 || M == 1){
			cout << "Case #" << q + 1 << ": YES" << endl;
		} else{
			FOR(i, 0, N){
				int cnt = 0;
				VI temp(M);
				FOR(j, 0, M)
					if(in[i][j] == in[i][0]){
						cnt++;
						temp[j] = in[i][0];
					}
				if(cnt == M)
					cur[i] = temp;
			}

			FOR(i, 0, M){
				int cnt = 0;
				VI temp(N);
				FOR(j, 0, N)
					if(in[j][i] == in[0][i]){
						cnt++;
						temp[j] = in[j][0];
					}
				if(cnt == N)
					FOR(j, 0, N)
						cur[j][i] = in[0][i];
			}

			for(int i = N - 1; i >= 0; i--){
				int cnt = 0;
				VI temp(M);
				for(int j = M - 1; j >= 0; j--)
					if(in[i][j] == in[i][M - 1]){
						cnt++;
						temp[j] = in[i][M - 1];
					}
				if(cnt == M)
					cur[i] = temp;
			}


			for(int i = M - 1; i >= 0; i--){
				int cnt = 0;
				VI temp(N);
				for(int j = N - 1; j >= 0; j-- )
					if(in[j][i] == in[N - 1][i]){
						cnt++;
						temp[j] = in[N - 1][i];
					}
				if(cnt == N)
					FOR(j, 0, N)
						cur[j][i] = in[N - 1][i];
			}
		
			bool ans = 1;
			FOR(i, 0, N)
				FOR(j, 0, M)
					if(cur[i][j] != in[i][j]){
						ans = 0;
						break;
					}
			string res;
			if(ans)
				res = "YES";
			else res = "NO";

			cout << "Case #" << q + 1 << ": " << res << endl;
		}
	}


	return 0;
}