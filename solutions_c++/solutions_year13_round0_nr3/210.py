#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector< vector<int> > table;
vector<int> now, nxt, t2, c, a, A, B;

bool inline squ(vector<int> x)
{
	c.clear();
	c.resize(x.size() * 2 - 1, 0);
	//puts("c OK!!!");
	for(int i = 0; i < x.size(); i++)
		for(int j = 0; j < x.size(); j++)
			c[i + j] += x[i] * x[j];
	
	//puts("multi OK!!!!");
	for(int i = 0; i < c.size(); i++)
		if(c[i] >= 10)
			return false;
	return true;
}

void inline dfs(int l)
{
	if(l == 0)
	{
		now.push_back(1);
		dfs(l + 1);
		now.pop_back();
		
		now.push_back(2);
		dfs(l + 1);
		now.pop_back();
		return ;
	}
	if(l == 26)
		return ;
	
	//printf("%d\n", l);
	bool fl = 0;
	nxt = now;
	//reverse(nxt.begin(), nxt.end());
	
	//puts("nxt finish!!!!!");
	
	a.clear();
	a = now;
	for(int i = nxt.size() - 1; i >= 0; i--)
		a.push_back(nxt[i]);
	//puts("going to squ!!!!");
	
	if(squ(a))
	{
		//puts("after squ!!!");
		table.push_back(c);
		fl = 1;
		//puts("A__A");
	}
	
	//puts("even finish!!!!!");
	
	for(int i = 0; i < 3; i++)
	{
		a.clear();
		a = now;
		a.push_back(i);
		for(int j = nxt.size() - 1; j >= 0; j--)
			a.push_back(nxt[j]);
		if(squ(a))
			table.push_back(c), fl = 1;//, puts("A__A");
	}
	
	if(!fl)
		return ;
	
	now.push_back(0);
	dfs(l + 1);
	now.pop_back();
	
	now.push_back(1);
	dfs(l + 1);
	now.pop_back();
}

bool inline cmp(vector<int> a, vector<int> b)
{
	if(a.size() != b.size())
		return a.size() < b.size();
	return a < b;
}

int main()
{
	//int t;
	//freopen("table.txt", "w", stdout);
	now.push_back(1);
	table.push_back(now);
	now[0] = 4;
	table.push_back(now);
	now[0] = 9;
	table.push_back(now);
	now.clear();
	//printf("START!!!!\n");
	dfs(0);
	//printf("%d\n", table.size());
	sort(table.begin(), table.end(), cmp);
	/*
	for(int i = 0; i < table.size(); i++)
	{
		for(int j = 0; j < table[i].size(); j++)
			printf("%d", table[i][j]);
		puts("");
	}
	*/
	//sort(table.begin(), table.end(), cmp);
	freopen("C-large-2.in", "r", stdin);
	freopen("C-large-2.out", "w", stdout);
	int t;
	cin >> t;
	for(int Case = 1; Case <= t; Case++)
	{
		string in1, in2;
		printf("Case #%d: ", Case);
		cin >> in1 >> in2;
		A.clear(), B.clear();
		for(int i = 0; i < in1.length(); i++)
			A.push_back(in1[i] - '0');
		for(int i = 0; i < in2.length(); i++)
			B.push_back(in2[i] - '0');
		int num = 
		upper_bound(table.begin(), table.end(), B, cmp) -
		lower_bound(table.begin(), table.end(), A, cmp);
		printf("%d\n", num);
	}	
}
