#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <ctype.h>
#include <cassert>
#include <stack>
#include <fstream>

using namespace std;

#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left

template < typename T > T abs(T x)
{
	return x > 0 ? x : -x;
}


string str[20];
vector < int > a[20];
int n, m;
int ans = 0;
int ans2 = 0;



struct node
{
	map < char, node* > nxt;
	bool term;
	node ()
	{
		term = false;
	}
};

int res2[1 << 9];


int build(const vector < int > &v)
{
	if (v.empty())
		return 0;
	node *root = new node();
	vector < node * > vv;
	vv.pb(root);
	int res = 1;
	for (int i = 0; i < v.size(); i++)
	{
		for (int j = 0; j < str[v[i]].size(); j++)
		{
			node *curr = root;
			for (int h = 0; h <= j; h++)
			{
				if (curr->nxt.find(str[v[i]][h]) == curr->nxt.end())
				{
					curr->nxt[str[v[i]][h]] = new node();
					//res++;
					vv.pb(curr->nxt[str[v[i]][h]]);
				}
				curr = curr->nxt[str[v[i]][h]];
			}
			if (!curr->term)
			{
				res++;
				curr->term = true;
			}
		}
	}
	
	for (int i = 0; i < vv.size(); i++)
		delete vv[i];
	
	return res;
}

void rec(int p)
{
	if (p == -1)
	{
		int sum = 0;
		for (int i = 0; i < n; i++)
		{
			int mask = 0;
			for (int j = 0; j < a[i].size(); j++)
				mask |= 1 << a[i][j];
			if (mask == 0)
				return;
			sum += res2[mask];
		}
		
		if (sum > ans)
		{
			//cerr << sum << endl;
			ans = sum;
			ans2 = 1;
			
		}
		else if (sum == ans)
			ans2++;
			
		return;
	}
	
	for (int i = 0; i < n; i++)
	{
		a[i].pb(p);
		rec(p - 1);
		a[i].pop_back();
	}
}



int main(int argc, char *argv[])
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int t;
	scanf("%d\n", &t);
	
	for (int tt = 1; tt <= t; tt++)
	{
		cerr << tt << endl;
		cin >> m >> n;
		
		for (int i = 0; i < m; i++)
		{
			cin >> str[i];
			//cerr << str[i] << endl;
		}
			
		for (int i = 0; i < (1 << m); i++)
		{
			vector < int > v;
			for (int j = 0; j < m; j++)
				if (i & (1 << j))
					v.pb(j);
			
			res2[i] = build(v);
		}
		
		
		ans = 0;
		ans2 = 0;
		
		rec(m - 1);
		
		cout << "Case #" << tt << ": " << ans << " " << ans2 << endl;
	}
	return 0;
}













