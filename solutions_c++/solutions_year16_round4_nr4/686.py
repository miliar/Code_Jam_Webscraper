#include <iostream> 
#include <vector> 
#include <string> 
#include <algorithm> 
#include <sstream> 
#include <set> 
#include <map> 
#include <queue> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <bitset> 
#include <unordered_map> 
#include <unordered_set> 

using namespace std;
typedef long long ll;

vector < vector<int>  >v;

vector<int> perm;
vector<vector<int> > know;
int n;
bool dfs(int ptr, int msk)
{
	if (ptr == n - 1)
	{
		for (int i = 0; i < know[perm[ptr]].size(); ++i)
		{
			int q = know[perm[ptr]][i];
			if (!(msk & (1 << q)))
			{
				return true;
			}
		}
		return false;
	}

	bool fl = true;
	if (know[perm[ptr]].size() == 0)
		return false;
	bool was = false;
	for (int i = 0; i < know[perm[ptr]].size(); ++i)
	{
		int q = know[perm[ptr]][i];
		if (!(msk & (1 << q)))
		{
			was = true;
			fl *= dfs(ptr + 1, msk | (1 << q));
			if (fl == false)
				return false;
		}
	}
	if (was == false)
		return false;
	return fl;
}

int check(vector<vector<int> > tmp)
{
	know.clear();
	perm.clear();
	perm.resize(n);
	know.resize(n);
	for (int i = 0; i < n; ++i)
	{
		perm[i] = i;
		for (int j = 0; j < n; ++j)
		{
			if (tmp[i][j])
				know[i].push_back(j);
		}
	}

	bool fl = true;
	sort(perm.begin(), perm.end());
	do
	{
		fl *= dfs(0, 0);

	} while (next_permutation(perm.begin(), perm.end()));
	if (fl == false)
		return 1e9;
	int ans = 0;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			if (tmp[i][j] < v[i][j])
				return 1e9;
			if (tmp[i][j] > v[i][j])
			{
				ans++;
			}
		}
	}
	return ans;
}

int main() {
#ifdef _CONSOLE 
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		
		cin >> n;
		v.clear();
		v.resize(n, vector<int> (n,0));
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				char c;
				cin >> c;
				if(c == '1')
					v[i][j] = 1;
			}
		}

		int k = n*n;
		int ans = 1e9;
		for (int i = 0; i < (1 << k); ++i)
		{
			vector<vector<int> > tmp(n, vector<int>(n, 0));
			int ptr = 0;
			for (int j = 0; j < n; ++j)
			{
				for (int m = 0; m < n; ++m)
				{
					if (i & (1 << ptr))
					{
						tmp[j][m] = true;
					}
					ptr++;
				}
			}

			int cost = check(tmp);
			ans = min(ans, cost);
		}

		cout << "Case #" << t << ": " << ans << "\n";

	}


	return 0;
}

