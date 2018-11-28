#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <algorithm>
#define MOD 1000000007
#define forn(a, n) for(int a = 0; a<(int) (n); ++a)
#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define forall(a, all) for(__typeof(all.begin()) a = all.begin(); a != all.end(); ++a)
#define EPS 0.000000000001
typedef long long tint;
using namespace std;

double DP[256][256];
double P[256];
double ch[256];

int main()
{
#ifdef ACMTUYO
  freopen("B-large (2).in", "r", stdin);
  freopen("B-large (2).out", "w", stdout);
#endif

	int T;
  cin >> T;
  forn(tc,T)
  {
    int N, K;
    cin >> N >> K;
    forn(i, N) {
		cin >> P[i];
    }
    
    sort(P, P+N);
    
    double ans = 0;
    forn(c, K+1) {
		
		memset(ch, 0 ,sizeof(ch));
		forn(i, c)
		{
			ch[i] = P[i];
		}
		
		forn(i, K-c) {
			ch[i+c] = P[N-i-1];
		}
	
		memset(DP, 0, sizeof(DP));
		DP[0][0]=1;
		forn(i, K)
		{
			forn(j, K)
			{
				DP[i+1][j]=DP[i][j]*(1-ch[i]);
				if(j)
					DP[i+1][j]+=DP[i][j-1]*ch[i];
			}
		}
		ans = max(ans, DP[K][K/2]);
	}
    cout << "Case #" << tc+1 << ": ";
    printf("%.9f", ans);
    cout << "\n";
  }
}
