#pragma comment(linker, "/STACK:134217728")
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <cmath>
#include <list>
#include <iomanip>
#include <set>
#include <map>
using namespace std;
#define RFor(i,a,b) for(int (i)=(a);(i)>=(b);--(i)) 
#define For(i,a,b) for(int (i)=(a);i<=(b);++(i))
#define FOR(i,a,b) for(int (i)=(a);i<(b);++(i))
#define RFOR(i,a,b) for(int (i)=(a)-1;(i)>=(b);--(i)) 
#define ll long long
#define ull unsigned long long
#define UI unsigned int
#define LD long double
#define pii pair<int,int>
#define mp make_pair
#define MOD 1000000007
//#define x first
//#define y second
int n,m;
int arr[150][150] = { 0 };
int maxn[150] = { 0 };
int maxm[150] = { 0 };
bool boo = false;

int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t;
	scanf("%d",&t);
	for (unsigned i = 0; i < t; ++i)
	{
		scanf("%d%d", &n, &m);
		memset(maxn, 0, sizeof(maxn));
		memset(maxm, 0, sizeof(maxm));
		for (unsigned j = 0; j < n; ++j)
			for (unsigned k = 0; k < m; ++k)
			{
				scanf("%d", &arr[j][k]);
				if(arr[j][k] > maxn[j]) maxn[j] = arr[j][k];
				if(arr[j][k] > maxm[k]) maxm[k] = arr[j][k];
			}

			boo = true;
		cout << "Case #" << i + 1 << ": ";
		for (unsigned j = 0; j < n; ++j)
			for (unsigned k = 0; k < m; ++k)
			{
				if(arr[j][k] != maxn[j] && arr[j][k] != maxm[k])
				{
					boo = false;
					goto label1;
				}
			}
label1:;
			if (boo) cout << "YES\n";
			else cout << "NO\n";
	}
	return 0;
}