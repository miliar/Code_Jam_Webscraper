#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

const int MAXN = 1010;
const int md = 1000000007;

int m, n;

string ss[10];
int b[10];
int ret, ren;
set<string> st;

int Calc()
{
	int ret = 0;
	for (int k = 0; k < n; k ++)
	{
		bool emp = true;
		for (int i = 0; i < m; i ++)
			if (b[i] == k)  emp = false;
		if (emp) return 0;
	} 
	for (int k = 0; k < n; k ++)
	{
		st.clear();
		st.insert("");
		for (int i = 0; i < m; i ++)
			if (b[i] == k)
			{
				string sv = "";
				for (int j = 0; j < ss[i].length(); j ++)
				{
					sv += ss[i][j];
					st.insert(sv);
				}
			}
		ret += st.size();
	}
	return ret;
}

void Dfs(int s)
{
	if (s >= m)
	{
		int z = Calc();
		if (z > ret)
		{
			ret = z;  ren = 1;
		}
		else if (z == ret)  ren ++;
		return;
	}
	for (int i = 0; i < n; i ++)
	{
		b[s] = i;
		Dfs(s + 1);
	}
}

void Work()
{
	cin >> m >> n;
	for (int i = 0; i < m; i ++)
		cin >> ss[i];
	ret = 0;  ren = 0;
	Dfs(0);
	cout << ret << " " << ren;
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	cin.sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt ++)
	{
		cout << "Case #" << tt << ": ";
		Work();
		cout << endl;
	}
	return 0;
}