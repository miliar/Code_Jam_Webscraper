#include <iostream>
#include <map>
#include <vector>

using namespace std;

const int MAXN = 22;
const int MAXW = MAXN * 10 + 2000;

map<string, int> mp;
int cntr = 0;
vector<int> v[MAXN];
int cnt[MAXW];

int get(string &s)
{
	if (mp.find(s) == mp.end())
		mp[s] = cntr++;
	return mp[s];
}

int main()
{
	int tt;
	cin >> tt;
	for (int tc = 1; tc <= tt; tc++)
	{
		int n;
		cin >> n;
		cin.ignore();
		mp.clear();
		cntr = 0;
		for (int i = 0; i < n; i++)
		{
			v[i].clear();
			string t;
			getline(cin, t);
			string word = "";
			for (int j = 0; j < t.length(); j++)
				if (t[j] == ' ')
				{
					v[i].push_back(get(word));
					word = "";
				}
				else
					word += t[j];
			v[i].push_back(get(word));
		}
		int ans = cntr;
		for (int i = 0; i < (1 << n); i++)
		{
			for (int j = 0; j < cntr; j++)
				cnt[j] = 0;
			if ((i & 1) || ((i & 2) == 0))
				continue;
			for (int j = 0; j < n; j++)
			{
				int cur = (i >> j) & 1;
				for (int k = 0; k < v[j].size(); k++)
					cnt[v[j][k]] |= cur + 1;
			}
			int cura = 0;
			for (int j = 0; j < cntr; j++)
				if (cnt[j] == 3)
					cura++;
			ans = min(ans, cura);
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}

}
