#include <iostream>
#include <string>
#include <iomanip>
#include <stdio.h>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; ++i)
#define rep2(i, x, n) for (int i = x; i < n; ++i)
#define repd(i, n) for (int i = n - 1; i >= 0; --i)
#define repd2(i, x, n) for (int i = n - 1; i >= x; --i)
#define _(a, b) memset(a, b, sizeof(a))
int ri() { int a; scanf( "%d", &a ); return a; }
double rf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; 
string rs() { scanf( "%s", sbuf ); return sbuf; }
long long rll() { long long a; scanf( "%lld", &a ); return a; }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;
typedef map<string,string> mss;

bool Check(int key[], int totalneedkey[], int totalprodkey[], int N)
{
	rep(i, N)
		if (key[i] + totalprodkey[i] < totalneedkey[i])
			return false;
	return true;
}
bool Solve(vector<int> &res, int key[], int totalneedkey[], vector<int> &need, const vector<vector<int>> &prod, 
		   int opened, int N)
{
	if (opened == N)
		return true;

	rep(i, need.size())
	{
		int origneed = need[i];
		if (origneed != 0 && key[origneed] > 0)
		{
			int p = 0;
			rep(j, prod[i].size()) p = (prod[i][j] == origneed) ? (p+1) : p;
			if (key[origneed] == 1 && p == 0 && totalneedkey[origneed] == 2) // last one and cannot produce
			{
				bool allow = true;
				rep2(j, i+1, need.size())
				{
					if (need[j] == 0)
						continue;
					rep(k, prod[j].size())
					{
						if (prod[j][k] == origneed && need[j] != origneed)
							goto go;
					}
				}
				allow = false;
go:
				if (!allow)
					continue;
			}
			res.push_back(i+1);
			key[origneed]--;
			totalneedkey[origneed]--;
			need[i] = 0;
			rep(j, prod[i].size())
			{
				key[prod[i][j]]++;
			}
			if (Solve(res, key, totalneedkey, need, prod, opened+1, N))
			{
				return true;
			}
			else
			{
				res.pop_back();
				need[i] = origneed;
				key[origneed]++;
				totalneedkey[origneed]++;
				rep(j, prod[i].size())
				{
					key[prod[i][j]]--;
				}
			}
		}
	}
	return false;
}
int main()
{
	freopen("C:\\Users\\Administrator\\Desktop\\D-small-attempt3.in","rt",stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\_Output.out","wt",stdout);
	
	int T = ri();
	rep(t, T)
	{
		int K = ri();
		int N = ri();
		int key[210];
		int totalneedkey[210];
		int totalprodkey[210];
		_(key, 0);
		_(totalneedkey, 0);
		_(totalprodkey, 0);
		rep(i, K) key[ri()]++;
		vector<int> need;
		vector<vector<int>> prod;
		rep(i, N)
		{
			int ne = ri();
			totalneedkey[ne]++;
			need.push_back(ne);
			int p = ri();
			vector<int> pp;
			rep(j, p){
				pp.push_back(ri());
				totalprodkey[pp.back()]++;
			}
			prod.push_back(pp);
		}
		bool succeed = false;
		vector<int> res;
		if (Check(key, totalneedkey, totalprodkey, N))
		{
			succeed = Solve(res, key, totalneedkey, need, prod, 0, N);
		}
		printf("Case #%d:", t+1);
		if (succeed)
		{
			rep(i, res.size()) printf(" %d", res[i]);
			printf("\n");
		}
		else
		{
			printf(" IMPOSSIBLE\n");
		}
	}
	return 0;
}








