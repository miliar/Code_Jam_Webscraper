#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <cstring>
#include <queue>
#include <deque>
#include <functional>
#include <climits>
#include <cassert>
#include <list>
#include <sstream>
#include <unordered_set>
#include <unordered_map>

#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))
#define ABS(a) (((a) > 0) ? (a) : (-(a)))
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))

using namespace std;
typedef long long ll;

ll get_hash(string& s)
{
	const ll P = 53;
	ll h = 0;
	ll curP = 1;
	for (int i = 0; i < s.length(); i++)
	{
		h += (s[i] - 'a' + 1) * curP;
		curP *= P;
	}
	return h;
}

vector<ll> read_sentence()
{
	vector<ll> res;
	string s;
	getline(cin, s);
	stringstream ss;
	ss << s;
	
	string cur;
	while (ss >> cur)
		res.push_back(get_hash(cur));
	
	return res;
}

vector<int> was_eng;
vector<int> was_fra;

int cur;
unordered_map<ll, int> m;

vector<vector<int> > indexes;

void add_sentence(int ind, vector<ll>& v, bool isen, int mask)
{
	for (int i = 0; i < v.size(); i++)
	{

		int w = indexes[ind][i];

		if (was_eng[w] == was_fra[w] && was_eng[w] == mask) continue;

		if (isen)
			was_eng[w] = mask;
		else
			was_fra[w] = mask;
		if (was_eng[w] == was_fra[w])
			cur++;

	}
}

int get_inters_count(unordered_set<ll>& a, unordered_set<ll>& b)
{
	int res = 0;
	for (auto& el : a)
	{
		if (b.count(el))
			res++;
	}
	return res;
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	cin >> t;

	for (int q = 0; q < t; q++)
	{
		int n;
		cin >> n;
		vector<vector<ll> > v;
		string tempstringnothingdoto;
		getline(cin, tempstringnothingdoto);
		for (int i = 0; i < n; i++)
		{
			vector<ll> e = read_sentence();
			if (i > 1)
			{
				if (e == v[0] || e == v[1]) continue;
			}
			v.push_back(e);
		}
		n = v.size();
		int ans = 2e9;
		vector<ll> words_list;
		set<ll> S;
		
		for (int i = 0; i < v.size(); i++)
		{
			for (int j = 0; j < v[i].size(); j++)
				S.insert(v[i][j]);
		}

		for (auto& el : S)
		{
			m[el] = words_list.size();
			words_list.push_back(el);
		}

		was_eng.resize(words_list.size());
		was_fra.resize(words_list.size());
		indexes.resize(n);

		for (int i = 0; i < indexes.size(); i++)
		{
			indexes[i].resize(v[i].size());
			for (int j = 0; j < indexes[i].size(); j++)
				indexes[i][j] = m[v[i][j]];
		}

		for (int i = 0; i < words_list.size(); i++)
		{
			was_eng[i] = was_fra[i] = -1;
		}

		for (int mask = 0; mask < (1 << (n - 2)); mask++)
		{
			if (ans == 0) break;
			cur = 0;
			for (int i = 0; i < n; i++)
			{
				if (cur >= ans) break;
				if (i == 0)
					add_sentence(0, v[0], 1, mask);
				else if (i == 1)
					add_sentence(1,v[1], 0, mask);
				else
				{
					int ind = i - 2;
					if ((mask >> ind) & 1)
						add_sentence(i,v[i], 1, mask);
					else
						add_sentence(i,v[i], 0, mask);
				}
			}
			ans = min(ans, cur);
		}
		printf("Case #%d: %d\n", q + 1, ans);
	}

	return 0;
}