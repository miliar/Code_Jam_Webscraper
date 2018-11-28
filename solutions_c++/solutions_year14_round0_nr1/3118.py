#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <set>
using namespace std;

int first[4][4];
int second[4][4];
int firstanswer, secondanswer;
set<int> ans;
int solve()
{
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			if(first[firstanswer-1][i] == second[secondanswer-1][j])
			{
				ans.insert(first[firstanswer-1][i]);
				break;
			}
		}
	}
	if(ans.size() == 1)
	{
		return *(ans.begin());
	}
	else if(ans.size() > 1)
	{
		return -1;
	}
	else if(ans.empty())
	{
		return 0;
	}
}

int initdata()
{
	memset(first, 0, sizeof(first));
	memset(second, 0, sizeof(second));
	firstanswer = secondanswer = 0;
	ans.clear();
	return 0;
}

int inputdata()
{
	cin >> firstanswer;
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			cin >> first[i][j];
		}
	}
	cin >> secondanswer;
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			cin >> second[i][j];
		}
	}
	return 0;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("A-small-attempt1.in", "r", stdin);
	//freopen("A-small.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t=0; t<T; t++)
	{	
		initdata();
		inputdata();
		int ret = solve();
		if(ret > 0 )
			printf("Case #%d: %d\n", t+1, ret);
		else if(ret == -1)
			printf("Case #%d: Bad magician!\n", t+1);
		else if(ret == 0)
			printf("Case #%d: Volunteer cheated!\n", t+1);

	}
	return 0;
}

