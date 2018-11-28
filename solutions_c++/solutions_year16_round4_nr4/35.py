#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>

using namespace std;
typedef long long ll;
const int MAXN = 30;
const int MAXP = (1 << 16);

ifstream fin ("D.in");
ofstream fout ("D.out");

int N, P, K;
int parent[MAXN];
int sz[MAXN], rsz[MAXN];

pair <int, int> pval[MAXN];
int dp[MAXP][MAXN];

int cfind (int x)
{
	if (x == parent[x]) return x;
	return parent[x] = cfind (parent[x]);
}

void uni (int x, int y)
{
	x = cfind (x);
	y = cfind (y);
	parent[x] = y;
}

int main()
{
    int ntest = 0; fin >> ntest;
    for (int test = 1; test <= ntest; test++)
    {
    fin >> N;
    for (int i = 0; i < N; i++)
    {
    	sz[i] = rsz[i] = 0;
    	parent[i] = i;
    }

    int tot = 0;
    string s;
    for (int i = 0; i < N; i++)
    {
    	fin >> s;
    	for (int j = 0; j < N; j++)
    		for (int k = 0; k < j; k++)
    			if (s[j] == '1' && s[k] == '1')
    				uni (j, k);

		for (int j = 0; j < N; j++)
			if (s[j] == '1')
				tot++;
		for (int j = 0; j < N; j++)
			if (s[j] == '1')
			{
				rsz[j]++;
				break;
			}
    }

    for (int i = 0; i < N; i++)
    {
    	sz[cfind (i)]++;
    	if (i != cfind (i))
    	{
    		rsz[cfind (i)] += rsz[i];
    		rsz[i] = 0;
    	}
    }

    P = K = 0;
    int stot = 0;
    for (int i = 0; i < N; i++)
    {
    	if (sz[i])
    	{
    		if (rsz[i] == 0)
    			K++;
    		else
    		{
    			if (rsz[i] == sz[i])
    			{
    				stot += sz[i] * sz[i];
    			}
    			else
    			{
    				pval[P++] = make_pair (rsz[i], sz[i]);
    			}
    		}
    	}
    }

    for (int i = 0; i < (1 << P); i++)
    	for (int j = 0; j <= K; j++)
    		dp[i][j] = 1e6;
    dp[(1 << P) - 1][K] = 0;

    for (int i = (1 << P) - 1; i > 0; i--)
    {
    	vector <int> loc;
    	for (int j = 0; j < P; j++)
    		if (i & (1 << j))
    			loc.push_back (j);

    	int m = loc.size();

		for (int j = 0; j <= K; j++)
			if (dp[i][j] < 1e5)
			{
				for (int k = 0; k < (1 << (m - 1)); k++)
				{
					int ltot = 0, rtot = 0, chash = 1 << (loc[m-1]);
					for (int l = 0; l < m - 1; l++)
						if (k & (1 << l))
						{
							ltot += pval[loc[l]].first;
							rtot += pval[loc[l]].second;
							chash += (1 << loc[l]);
						}
					ltot += pval[loc[m-1]].first;
					rtot += pval[loc[m-1]].second;

					int nk = j;
					if (rtot < ltot)
					{
						nk -= ltot - rtot;
						rtot = ltot;
					}

					if (nk >= 0)
						dp[i - chash][nk] = min (dp[i - chash][nk], dp[i][j] + rtot * rtot);
				}
			}
    }

    int res = 1e6;
    for (int i = 0; i <= K; i++)
    	res = min (res, dp[0][i] + i);

    fout << "Case #" << test << ": ";
    //fout << tot << " " << res << " " << stot << " ";
    fout << res + stot - tot << "\n";
    }
    return 0;
}

