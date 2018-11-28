#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

vector<string> a;
vector<string> sets[5];
char tmp[50];
int n, m;
int ans1 = 0, ans2 = 0;

struct Node{
	Node *next[27];
	bool end;
	
	void garante(char c)
	{
		if(next[c - 'A'] == NULL)
			next[c - 'A'] = (Node *) calloc(sizeof(Node), 1);
	}
	
	void insert(const char s[], int i)
	{
		if(s[i] == '\0')
			end = true;
		else
		{
			garante(s[i]);
			next[s[i]-'A']->insert(s, i+1);
		}
	}
	
	int dfs()
	{
		int retv = 1;
		for(int i = 0; i < 26; i++)
			if(next[i])
			{
				retv += next[i]->dfs();
			}
		return retv;
	}
	
		
	void erase()
	{
		for(int i = 0; i < 26; i++)
			if(next[i])
			{
				next[i]->erase();
				free(next[i]);
			}
	}
};
 

int f(vector<string> x)
{
	Node *root =(Node *) calloc(sizeof(Node), 1);
	for(int i = 0; i < x.size(); i++)
		root->insert(x[i].c_str(), 0);
	int retv = root->dfs();
	root->erase();
	return retv;
}

void foo(int i)
{
	if(i == n)
	{
		for(int j = 0; j < m; j++)
			if(sets[j].empty())
				return;
		int x = 0;
		for(int j = 0; j < m; j++)
			x += f(sets[j]);
		if(x > ans1)
		{
			ans1 = x;
			ans2 = 1;
		}
		else if(x == ans1)
		{
			ans2++;
		}
		return;
	}
	for(int j = 0; j < m; j++)
	{
		sets[j].push_back(a[i]);
		foo(i+1);
		sets[j].pop_back();
	}
}

int
main(void)
{
	int t;
	scanf("%d", &t);
	for(int T = 1; T <= t; T++)
	{
		ans1 = 0;
		ans2 = 0;
		a.clear();
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; i++)
		{
			scanf(" %s", tmp);
			a.push_back(tmp);
		}
		foo(0);
		printf("Case #%d: %d %d\n", T, ans1, ans2);
	}
}
