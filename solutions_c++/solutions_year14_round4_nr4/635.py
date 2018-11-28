#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <algorithm> 
#include <vector> 
#include <string> 
#include <iostream> 
#include <sstream> 
#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <fstream> 
#include <numeric> 
#include <iomanip> 
#include <bitset> 
#include <list> 
#include <stdexcept> 
#include <functional> 
#include <utility> 
#include <ctime>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MEM(a,b) memset((a),(b),sizeof(a))
const double eps = 1e-10;
const int N = 10000;
const int M = 26;
char str[11];
int ans = 0;
class Trie
{
public:
	int ch[N][M];
	int val[N];
	int sz;
	Trie(){ sz = 1; MEM(ch[0], 0); MEM(val, 0); }
	int idx(char c)
	{
		if (isalpha(c)) return c - 'A';
	}
	void clear(){ sz = 1; MEM(ch[0], 0); MEM(val, 0); }
	void insert(const char *str, int x)
	{
		int u = 0, n = strlen(str);
		for (int i = 0; i < n; i++)
		{
			int c = idx(str[i]);
			if (!ch[u][c])
			{
				MEM(ch[sz], 0);
				ch[u][c] = sz++;
			}
			u = ch[u][c];
		}
		val[u] = x;

	}

	int find(char *str)
	{
		int u = 0;
		int l = strlen(str);
		int i;
		for (i = 0; i < l; i++)
		{
			int c = idx(str[i]);
			if (!ch[u][c]) return 0;
			u = ch[u][c];
		}
		return val[u];
	}
};
Trie tr;
vector<string> vs;
map<int, int> mm;
int main()
{
	//freopen("input.txt", "r", stdin);
	
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	/*freopen("B-large.in", "r", stdin);
		freopen("B-large.out", "w", stdout);*/

	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		int n, m;
		cin >> n >> m;
		int flag[10];
		vs.resize(n);
		for (int i = 0; i < n; i++) cin >> vs[i];
		MEM(flag, 0);
		mm.clear();
		while (1)
		{
			int sum = 0;
			map<int, int> mmm;
			for (int i = 0; i < n; i++) mmm[flag[i]] = 1;
			if (mmm.size() == m)
			{
				for (int i = 0; i < m; i++)
				{
					tr.clear();
					for (int j = 0; j < n; j++)
					{
						if (flag[j] == i) tr.insert(vs[j].c_str(), 0);
					}
					sum += tr.sz;
				}
				mm[sum]++;
			}
			
			flag[0]++;
			for (int i = 0; i < n; i++)
			{
				if (flag[i] == m) flag[i] = 0, flag[i + 1]++;
			}
			if (flag[n]) break;
		}
		printf("Case #%d: %d %d\n", ks++, mm.rbegin()->first,mm.rbegin()->second);
	}
	return 0;
}