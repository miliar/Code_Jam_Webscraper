#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <stack>
#include <cmath>
#include <queue>
using namespace std;

string x;
vector<string> v;
vector<int> assignment(100);
int N, M;

vector<set<string> > s(20); 

int evaluate()
{
	for (int i = 0; i < N; ++i)
	{
		s[i].clear();
	}
	for (int i = 0; i < M; ++i)
	{
		s[assignment[i]].insert("$");
	}
	for (int i = 0; i < N; ++i)
	{
		if (s[i].size() == 0) return 0;
	}
	for (int i = 0; i < M; ++i)
	{
		string tmp;
		for (int j = 0; j < v[i].length(); ++j)
		{
			tmp.push_back(v[i][j]);
			s[assignment[i]].insert(tmp);
		}
	}
	int out = 0;
	for (int i = 0; i < N; ++i)
	{
		out += s[i].size();
	}
	return out;
}

int a = -1, b = 0;

void handle(int x)
{
	if (x > a)
	{
		a = x;
		b = 0;
	}
	if (x == a)
	{
		++b;
	}
}

void assign(int x)
{

	if (x >= M)
	{
		int k = evaluate();
		handle(k);
		return;
	}
	for (int i = 0; i < N; ++i)
	{
		assignment[x] = i;
		assign(x + 1);
	}
}

void input()
{
	cin >> M >> N;
	v.clear();

	for (int i = 0; i < M; ++i)
	{
		cin >> x;
		v.push_back(x);
	}

	a = -1; b = 0;
	assign(0);
	printf("%d %d\n", a, b);
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int T;
	scanf("%d", &T);

	for (int test = 1; test <= T; ++test)
	{
		printf("Case #%d: ", test);
		input();
	}

	return 0;
}