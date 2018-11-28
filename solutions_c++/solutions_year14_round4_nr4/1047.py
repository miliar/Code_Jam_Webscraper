#include <iostream>
#include <fstream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <cmath>
#include <math.h>
#include <stdlib.h>

#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
using namespace std;
int T,M, N;
string s[10];
vector<string> vs[5];
int X, Y;
class Node
{
public:
	Node *child[26];
	Node(){
		for (int i=0;i<26;i++)
			child[i]=NULL;
	}
};
void add(Node *root, string vec)
{
	Node *tmp = root;
	for (int i=0;i<vec.length();i++)
	{
		if (!tmp->child[vec[i]-'A'])
		{
			tmp->child[vec[i]-'A'] = new Node();
		}
		tmp = tmp->child[vec[i]-'A'];
	}
}
Node *buildtrie(vector<string> &vec)
{
	Node *root = new Node();
	for (int i=0;i<vec.size();i++)
	{
		add(root, vec[i]);
	}
	return root;
}
int nodenum(Node *root)
{
	if (!root)
		return 0;
	int ans = 1;
	for (int i=0;i<26;i++)
		ans += nodenum(root->child[i]);
	return ans;
}
void deltrie(Node *root)
{
	if (!root)
		return;
	for (int i=0;i<26;i++)
		deltrie(root->child[i]);
	delete(root);
}
int cnttrie(vector<string> &vec)
{
	int ans = 0;
	Node *root = buildtrie(vec);
	ans += nodenum(root);
	deltrie(root);
	return ans;
}
int cnt()
{
	int ans = 0;
	for (int i=0;i<N;i++)
		ans += cnttrie(vs[i]);
	return ans;
}
void dfs(int cur)
{
	if (cur==M)
	{
		bool valid = true;
		for (int i=0;i<N;i++)
			if (vs[i].size()==0)
			{
				valid = false;
				break;
			}
		if (valid)
		{
			int ans = cnt();
			if (ans > X)
			{
				X = ans;
				Y = 1;
			}
			else if (ans == X)
				Y++;
		}
		return;
	}
	for (int i=0;i<N;i++)
	{
		vs[i].push_back(s[cur]);
		dfs(cur+1);
		vs[i].pop_back();
	}
}
int main()
{
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		scanf("%d%d",&M, &N);
		X = 0;
		Y = 0;
		printf("Case #%d: ",i);
		for (int j=0;j<M;j++)
		{
			cin>>s[j];
		}
		dfs(0);
		printf("%d %d\n",X, Y);
	}
	return 0;
}