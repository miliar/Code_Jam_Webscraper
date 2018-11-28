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

vector<vector<vector<int> > > solutions[5];

bool backtrack(vector<vector<int> > asig, vector<int> mask, int i, int j, int n, int quedan)
{
	if(i == n)
	{
		return quedan == 0;
	}
	
	if(i == j)
	{
		return backtrack(asig, mask, i+1, j, n, quedan);
	}
	
	bool ans = false;
	forn(k, n)
	{
		if(asig[i][k] && mask[k])
		{
			mask[k]=0;
			ans |= backtrack(asig, mask, i+1, j, n, quedan-1);
			mask[k]=1;
		}
	}
	ans |= backtrack(asig, mask, i+1, j, n, quedan);
	
	return ans;
}

int main()
{
#ifdef ACMTUYO
  freopen("D-small-attempt0 (1).in", "r", stdin);
  freopen("D-small-attempt0 (1).out", "w", stdout);
#endif

	int T;
  cin >> T;
  
  forn(i, 5)
  {
	  if(i)
	  {
		  forn(j, 1<<(i*i))
		  {
			  vector<vector<int> > asig(i, vector<int>(i, 0));
			  forn(k, i*i)
			  {
				  if(j&(1<<k))
				  {
					  asig[k/i][k%i]=1;
				  }
			  }
			  
			  bool anda = true;
			  forn(k, i)
			  {
				  vector<int> mask = asig[k];
				  int quedan = 0;
				  forn(r, i) if(mask[r]) quedan++;
				  if(backtrack(asig, mask, 0, k, i, quedan)) anda = false;
			  }
			  
			  if(anda)
			  {
				  solutions[i].push_back(asig);
			  }
		  }
	  }
  }
  
  forn(tc,T)
  {
    int N;
    cin >> N;
    vector<vector<int> > C(N, vector<int>(N, 0));
    vector<string> Inp(N);
    forn(i, N) cin >> Inp[i];
    forn(i, N) forn(j, N) C[i][j] = Inp[i][j]-'0';
    
    int ans=(1<<(N*N));
    
    forn(r, solutions[N].size())
    {
		vector<vector<int> > cand=solutions[N][r];
		int costo = 0;
		bool anda = true;
		forn(i, N) forn(j, N)
		{
			if(C[i][j] && !cand[i][j]) anda = false;
			costo += cand[i][j] - C[i][j];
		}
		if(anda) ans = min(ans, costo);
	}
    cout << "Case #" << tc+1 << ": ";
    cout << ans;
    cout << "\n";
  }
}
