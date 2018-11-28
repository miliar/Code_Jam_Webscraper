#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

char a[210][10100];
string b[210];
vector<string> vs[210];

int main()
{
	int t, kase = 0;
	cin.sync_with_stdio(false);
	cin >> t;
	while (t--)
	{
		cerr << kase << endl;

		int n;
		cin >> n;
		getchar();
		for (int i = 0; i < n; i++)
		{
			cin.getline(a[i], 10100);
			b[i] = a[i];
			istringstream in(b[i]);
			string str;
			vs[i].clear();
			while (in >> str)
				vs[i].push_back(str);
		}

		unordered_set<string> eb, fb;
		for (int i = 0; i < (int)vs[0].size(); i++)
			eb.insert(vs[0][i]);
		for (int i = 0; i < (int)vs[1].size(); i++)
			fb.insert(vs[1][i]);

		int base = 0;
		for (auto&it : eb)
		{
			if (fb.find(it) != fb.end())
				base++;
		}

		int extra = INT_MAX;
		for (int i = 0; i < (1 << (n - 2)); i++)
		{
			unordered_set<string> e, f;
			for (int j = 0; j < n - 2; j++)
			{
				if (i & (1 << j))
				{
					for (int k = 0; k < (int)vs[j + 2].size(); k++)
						e.insert(vs[j + 2][k]);
				}
				else
				{
					for (int k = 0; k < (int)vs[j + 2].size(); k++)
						f.insert(vs[j + 2][k]);
				}
			}

			unordered_set<string> s;
			for (auto&it : e)
			{
				if (eb.find(it) != eb.end()) continue;
				if (f.find(it) != f.end() || fb.find(it) != fb.end())
					s.insert(it);
			}

			for (auto&it : f)
			{
				if (fb.find(it) != fb.end()) continue;
				if (e.find(it) != e.end() || eb.find(it) != eb.end())
					s.insert(it);
			}
			if (s.size() < extra)
				extra = s.size();
		}
		cout << "Case #" << ++kase << ": " << base + extra << endl;
	}
	return 0;
}