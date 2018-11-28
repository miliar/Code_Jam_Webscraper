#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define repeat(t) for (int asdfg=0; asdfg < (t); asdfg++)
#define foreach(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define odd(x) (bool((x)&1))
#define even(x) (bool((x)&1^1))
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<vi> vvi;
typedef vector<pii> vpii;

int n,m;
int a[1100][1100],b[1100][1100];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);

	int cas;
	scanf("%d",&cas);
	for (int t=1; t<=cas; t++)
	{
		scanf("%d%d",&n,&m);
		for (int i=0; i<n; i++)
		{
			int x=0;
			for (int j=0; j<m; j++)
			{
				scanf("%d",&a[i][j]);
				if (a[i][j]>x) x=a[i][j];
			}
			for (int j=0; j<m; j++) b[i][j]=x;
		}

		bool flag=true;
		for (int j=0; j<m && flag; j++)
		{
			bool flag1=true;
			bool flag2=true;
			for (int i=0; i<n && flag1; i++) if (b[i][j]!=a[i][j])
				 flag1=false;
			if (flag1) continue;

			int x=100;
			for (int i=0; i<n; i++) if (b[i][j]!=a[i][j])
				x=min(x,a[i][j]);
			for (int i=0; i<n && flag2; i++) if (a[i][j]>x)
				 flag2=false;
			flag=flag2;
		}
		if (flag) printf("Case #%d: YES\n",t);
		else printf("Case #%d: NO\n",t);
	}
	return 0;
}