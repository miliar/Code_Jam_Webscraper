#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;



pair<string, string> mat[20][3];
bool solved[20][3];

bool mycomp(pair<string, string> x, pair<string, string> y)
{
	long long xa, xb, ya, yb;
	xa = atoll(x.first.c_str());
	xb = atoll(x.second.c_str());

	ya = atoll(y.first.c_str());
	yb = atoll(y.second.c_str());

	long long diff1 = llabs(xa - xb);
	long long diff2 = llabs(ya - yb);

	if (diff1 < diff2) return true;
	else if (diff2 < diff1) return false;
	else
	{
		if (xa < ya) return true;
		else if (xa > ya) return false;
		else
		{
			return xb < yb;
		}
	}
}



pair<string, string> make_great(string & a, string & b, int ind)
{

	pair<string, string> res("", "");
	for (int i = ind; i < a.length(); i++)
	{
		if (a[i] == '?') res.first += "0"; else res.first += a[i];
		if (b[i] == '?') res.second += "9"; else res.second += b[i];
	}

	return res;
}

pair <string, string> get_ans(string & a, string & b, int ind, int type)
{
	if (ind > a.size()) return make_pair("", "");
	if (solved[ind][type]) return mat[ind][type];

	if (type == 0)
	{
		//try the three options
		vector <pair<string, string> > v;
		

		for (int i = 0; i <= 9 ; i++)
		{
			char orig = a[ind];
			if (a[ind] == '?') a[ind] = '0' + i;
			for (int j = 0; j <= 9 ; j++)
			{
				char orig2 = b[ind];
				if (b[ind] == '?') b[ind] = '0' + j;

				pair <string, string> ans;
				if (a[ind] == b[ind]) ans = get_ans(a, b, ind + 1, 0);
				else if (a[ind] > b[ind]) ans = get_ans(a, b, ind + 1, 1);
				else ans = get_ans(a, b, ind + 1, 2);

				ans.first = a[ind] + ans.first;
				ans.second = b[ind] + ans.second;
				v.push_back(ans);

				b[ind] = orig2;
				if (b[ind] != '?') break;
			}
			a[ind] = orig;
			if (a[ind] != '?')  break;
		}

		sort(v.begin(), v.end(), mycomp);
		mat[ind][type] = v[0];
	}
	else if (type == 1) //a > b
	{
		mat[ind][type] = make_great(a, b, ind);
		
	}
	else if (type == 2) // b > a
	{
		mat[ind][type] = make_great(b, a, ind);
		swap(mat[ind][type].first, mat[ind][type].second);
	}
	solved[ind][type] = true;
	return mat[ind][type];
}



int main()
{
#if !ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int t;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		string a, b;
		unsigned long long ai, bi;
		ai = bi = 0;
		cin >> a >> b;

		memset(solved, false, sizeof(solved));

		pair <string, string> ans = get_ans(a, b, 0, 0);
		
		cout << "Case #" << z << ": " << ans.first.substr(0, a.length()) << " " << ans.second.substr(0, a.length()) << endl;
	}
	return 0;
}