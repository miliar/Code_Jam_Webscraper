#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <map>
using namespace std;
#define Submit

int matrix[15][15];
vector<pair<int,int> > pos;
int n,m;
bool f(int r, int c)
{
	int i,j;
	int ok1 = 1, ok2 = 1;
	for(i = 1; i <= m; i++)
	{
		if(matrix[r][i] != 1)	ok1 = 0;
	}
	for(i = 1; i <= n; i++)
	{
		if(matrix[i][c] != 1) 	ok2 = 0;
	}
	if(ok1 || ok2)	return true;
	else return false;
}


int main()
{
	#ifdef Submit
	freopen("B-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
	#endif
	int t,times = 1,i,j;
	scanf("%d", &t);
	while(t--)
	{
		cin >> n >> m;
		pos.clear();
		for(i = 1; i <= n; i++)		
		for(j = 1; j <= m; j++)
		{
			cin >> matrix[i][j];
			if(matrix[i][j] == 1)	pos.push_back(make_pair(i,j));
		}
		int ok = 1;
		for(i = 0; i < pos.size(); i++)
		{
			if(!f(pos[i].first, pos[i].second))
			{
				ok = 0;
				break;
			}
		}
		printf("Case #%d: %s\n", times++, ok?"YES":"NO");
	}
	return 0;
}
				    