//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 14;
typedef long long ll;

char ch[3];
bool beat[3][3];

string make(int n, int root)
{
	if(!n)
	{
		string s;
		s += ch[root];
		return s;
	}
	for(int oth = 0; oth < 3; oth++)
	{
		if(beat[root][oth])
		{
			string s1 = make(n - 1, root);
			string s2 = make(n - 1, oth);
			return min(s1 + s2, s2 + s1);
		}
	}
}

int main()
{
	int _t = in();
	ch[0] = 'P';
	ch[1] = 'R';
	ch[2] = 'S';
	beat[0][1] = beat[1][2] = beat[2][0] = 1;

	string res[N][3];
	for(int i = 0; i < N; i++)
		for(int root = 0; root < 3; root++)
			res[i][root] = make(i, root);

	for(int t = 1; t <= _t; t++)
	{
		cout << "Case #" << t << ": ";
		int n = in();
		int p, r, s;
		cin >> r >> p >> s;
		bool done = 0;
		for(int root = 0; root < 3; root++)
		{
			string cur = res[n][root];
			int cnt[300] = {};
			for(char c : cur)
				cnt[c]++;
			if(cnt['P'] == p && cnt['R'] == r && cnt['S'] == s)
			{
				cout << cur << endl;
				done = 1;
				break;
			}
		}
		if(!done)
			cout << "IMPOSSIBLE" << endl;
	}
}
