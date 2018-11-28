#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

#define TRUE 1
#define FALSE 0

vector<string> grid;
bool check_vertical(char t)
{
	for(int i=0;i<4;i++)
	{
		int cnt=0;
		for(int j=0;j<4;j++)
			if(grid[j][i]==t || grid[j][i]=='T') cnt++;
		if(cnt==4) return TRUE;	
	}
	return FALSE;
}
bool check_horizontal(char t)
{
	for(int i=0;i<4;i++)
	{
		int cnt=0;
		for(int j=0;j<4;j++)
			if(grid[i][j]==t || grid[i][j]=='T') cnt++;
		if(cnt==4) return TRUE;	
	}
	return FALSE;
}
bool check_diagonal(char t)
{
	int cnt=0;
	for(int i=0;i<4;i++)
	{
		if(grid[i][i]==t || grid[i][i]=='T') cnt++;
		if(cnt==4) return TRUE;	
	}
	cnt=0;
	for(int i=0;i<4;i++)
	{
		if(grid[3-i][i]==t || grid[3-i][i]=='T') cnt++;
		if(cnt==4) return TRUE;	
	}
	return FALSE;
}
bool check_completion()
{
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(grid[i][j]=='.') return TRUE;
	return FALSE;
}
int main()
{
	//freopen("A-small.in","r",stdin);
	//freopen("A-small.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	string row;
	int cases,i;
	cin>>cases;
	for(i=1;i<=cases;i++)
	{
		for(int x=0;x<4;x++)
		{
			cin>>row;
			grid.push_back(row);
		}
		if(check_vertical('O') || check_horizontal('O') || check_diagonal('O'))
			printf("Case #%d: O won\n",i);
		else if(check_vertical('X') || check_horizontal('X') || check_diagonal('X'))
				printf("Case #%d: X won\n",i);
		else if(check_completion())
				printf("Case #%d: Game has not completed\n",i);
		else printf("Case #%d: Draw\n",i);
		grid.clear();
	}
    return 0;
}

