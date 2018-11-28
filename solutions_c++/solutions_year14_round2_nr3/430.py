#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int const Max = 11;
int n, m;
bool way[Max][Max];
string res, nine;
string kod[Max];

void magic(int v, int mask[], int par[], string ans)
{
	bool end = true;
	for (int i = 1; i <= n; i++)
		if (mask[i] == 0)
			end = false;
	if (end)
	{
		if (ans <= res)
			res = ans;
		return;
	}
	if (par[v] != -1)
		magic(par[v], mask, par, ans);
	for (int i = 1; i <= n; i++)
		if (way[v][i] && mask[i] == 0)
		{
			int new_mask[Max];
			for (int j = 0; j < Max; j++)
				new_mask[j] = mask[j];
			new_mask[i] = 1;
			int new_par[Max];
			for (int j = 0; j < Max; j++)
				new_par[j] = par[j];
			new_par[i] = v;
			string new_ans = ans + kod[i];
			magic(i, new_mask, new_par, new_ans);
		}
	return;
}

int main()
{
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int test = 1; test <= t; test++)
	{
		nine = "99999";
		cin >> n >> m;
		res = "";
		for (int i = 1; i <= n; i++)
			res += nine;
		for (int i = 0; i < Max; i++)
			for (int j = 0; j < Max; j++)
				way[i][j] = false;
		for (int i = 1; i <= n; i++)
			cin >> kod[i];
		for (int i = 1; i <= m; i++)
		{
			int x, y;
			cin >> x >> y;
			way[x][y] = true;
			way[y][x] = true;
		}
		int min_kod = 1;
		for (int i = 2; i <= n; i++)
			if (kod[i] < kod[min_kod])
				min_kod = i;

		int min_kod2 = 0;
		for (int i = 1; i <= n; i++)
			if (way[min_kod][i])
			{
				min_kod2 = i;
				break;
			}
		for (int i = min_kod2 + 1; i <= n; i++)
			if (way[min_kod][i])
			{
				if (kod[i] < kod[min_kod2])
					min_kod2 = i;
			}

		int maska[Max];
		for (int i = 0; i < Max; i++)
			maska[i] = 0;
		maska[min_kod] = 1;
		maska[min_kod2] = 1;

		int parent[Max];
		for (int i = 0; i < Max; i++)
			parent[i] = -1;
		parent[min_kod2] = min_kod;

		string t_ans = kod[min_kod] + kod[min_kod2];

		magic(min_kod2, maska, parent, t_ans);
		cout << "Case #" << test << ": " << res << endl;
	}
	return 0;
}