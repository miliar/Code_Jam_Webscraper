#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <ctime>
#include <iomanip>
#include <iterator>
#include <set>
#include <string>

#define ii <int , int>


#define mp make_pair
#define all(v) v.begin(),v.end()
#define loop(i, n) for (int i = 0; i < n; i++)
#define pb push_back
#define sz(v) (int)v.size()


using namespace std;

typedef long long ll;
typedef vector<int > vi;
typedef vector<vi> vvi;
typedef pair ii pii;
typedef vector <pii> vii;
typedef map ii mii;
typedef set <int > si;
typedef multiset <int > msi;
typedef multimap <int , int> mmi;
  

const ll nInf = -1000000000;
const ll pInf = 1000000000;
const ll mod  = 1000000007;
void solve();

int main()
{
       freopen( "input.txt", "r" , stdin);
       freopen( "output.txt", "w" , stdout);

	   int t;
	   scanf("%d", &t);
	   for (int i = 0;i < t; i++)
	   {
		   printf("Case #%d: ", i + 1);
		   solve();
	   }
	   return 0;
}
int grid[20][20];
int g[20][20];  
void solve()
{
	int r, c, n;
	int am = 0;
	scanf ("%d %d %d", &r, &c, &n);
	if (n == 0)
	{
		printf("0\n");
		return;
	}
	int ans = pInf;
	for (int i = 0;i < 20; i++)
	{
		for (int j = 0;j < 20; j++)
		{
			g[i][j] = 0;
		}
	}
	for (int i = 1; i <= (1 << (r * c)); i++)
	{
		int a[100];
		fill (a, a + 100, 0);
		int num = 0;
		int i1 = i;
		while (i1 > 0)
		{
			a[num++] = i1 % 2;//.pb(i1 % 2);
			i1 = i1 / 2;
		}
//		reverse(a.begin(), a.end());
		reverse(a, a + num);
		int c1 = 0;
		int sum1 = 0;
		for (int j = 0; j < num; j++)
		{
			sum1+=a[j];
		}
		if (sum1 != n)
			continue;
		for (int j  = 1; j <= r; j++)
		{
			for (int k = 1; k <= c; k++)
			{
				g[j][k] = a[c1++];
			}
		}
		int sum = 0;
		for (int j = 1;j <= r; j++)
		{
			for (int k = 1;k <= c; k++)
			{
				int count = 0;
				if (!g[j][k])
					continue;
				if (g[j - 1][k] == 1)
					count++;
				if (g[j + 1][k] == 1)
					count++;
				if (g[j][k - 1] == 1)
					count++;
				if (g[j][k + 1] == 1)
					count++;
	//			g[i][j] = count;
				sum += count;
			}
		}
		if (sum < ans)
			ans = sum;
	}
	printf("%d\n", ans / 2);
}
