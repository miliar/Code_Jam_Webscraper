#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <stack>
#include <sstream>
#include <cstring>
#include <numeric>
#include <ctime>

using namespace std;

#define pb push_back
#define sz(x) ((int) (x).size())
#define fo(i, n) for (int i = 0; i < (n); i++)
#define fo2(i, j, n) for (int i = j; i < (n); i++)
#define rfo(i, n) for (int i = (n) - 1; i >= 0; i--)
#define clr(x, y) memset(x, y, sizeof(x))
#define sqr(x) ((x) * (x))

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef long long ll;
typedef pair<ll,ll> pll;

const int maxN = 100, maxM = 100;

bool horizontal(char field[maxN][maxM], int n, int m, int i, int j)
{

	fo(x,m)
	{
		if (x != j && field[i][x] > field[i][j])
			return false;
	}

	return true;
}

bool vertical(char field[maxN][maxM], int n, int m, int i, int j)
{

	fo(x,n)
	{
		if (x != i && field[x][j] > field[i][j])
			return false;
	}

	return true;
}

int main()
{
	int T;
	cin >> T;
	
	fo(t,T)
	{

		char fields[maxN][maxM];
		int n,m;
		cin >> n >> m;

		fo(i,n)
			fo(j,m)
				cin >> fields[i][j];

		bool possible = true;

		fo(i,n)
			fo(j,m)
			{
				if ( ! horizontal(fields, n, m, i, j) && ! vertical(fields, n, m, i, j) )
				{
					possible = false;
					break;
				}
			}

		cout << "Case #" << t + 1 << ": " << (possible ? "YES" : "NO") << endl;

	}
}
