#include <iostream>
#include <cstdio>
#include <map>
#include <string>
using namespace std;
typedef long long lint;

void change(char &c)
{
	if (c == '-') c = '+';
	else c = '-';
}
map<string, int> M;
void solve(int test)
{
	string s;
	cin >> s;
	int answer = M[s];
	

	printf("Case #%d: %d\n", test, answer);
}
string Q[1000 * 1000 * 10];

map<string, string> par;

void rev(string &x, int l)
{
	for (int j = 0, k = l; j <= k; k--, j++)
	{
		swap(x[j], x[k]);
		change(x[j]);
		if (j != k) change(x[k]);
	}
}


void bfs(string x)
{
	Q[0] = x;
	M[x] = 0;
	int top = 0, tail = 1;
	int L = x.size();
	string xx;
	while (top < tail)
	{
		xx = x = Q[top++];
		int y = M[x];
		for (int i = 0; i < L; i++)
		{
			rev(x, i);
			if (!M.count(x))
			{
				M[x] = y + 1;
				Q[tail++] = x;
				par[x] = xx;
			}
			rev(x, i);
		}
	}
}
void show(string x)
{
	if (!par.count(x))
	{
		cout << x << endl;
		return;
	}
	cout << x << " > ";
	show(par[x]);

}

int main()
{
	int T;
	string s = "";
	for (int i = 1; i <= 11; i++)
	{
		s += "+";
		bfs(s);
	}


	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	//T = 1000*1000;
	for (int i = 1; i <= T; i++)
	{
		solve(i);
	}
	return 0;
}