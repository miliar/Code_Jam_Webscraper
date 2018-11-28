#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <map>
using namespace std;


char m[5][5];
vector<pair<int,int> > pos; 
bool f(char ch)
{
	int i,j;
	for(i = 0; i < pos.size(); i++)
		m[pos[i].first][pos[i].second] = ch;
	
	for(i = 0; i < 4; i++)
	{
		if(m[i][0] == ch && m[i][1] == ch
		 	&& m[i][2] == ch && m[i][3] == ch) 
			 return true;
	}
	
	for(i = 0; i < 4; i++)
	{
		if(m[0][i] == ch && m[1][i] == ch
		 	&& m[2][i] == ch && m[3][i] == ch) 
			 return true;
	}
	if(m[0][0] == ch && m[1][1] == ch
		&& m[2][2] == ch && m[3][3] == ch)	return true;
	if(m[0][3] == ch && m[1][2] == ch
		&& m[2][1] == ch && m[3][0] == ch)	return true;
		
	return false;
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int t,i,j,times = 1;
	scanf("%d",&t);
	while(t--)
	{
		
	 	getchar();
		pos.clear();
		int end = 1;
		for(i = 0; i < 4; i++)
	 	{
		 	for(j = 0; j < 4; j++)
		 	{
		 		scanf("%c", &m[i][j]);
		 		if(m[i][j] == 'T')	pos.push_back(make_pair(i,j));
		 		if(m[i][j] == '.')  end = 0; 
	 	 	}
		 	getchar();
	 	}
	 	
	 	
	 	printf("Case #%d: ", times++);
		if(f('X'))
		{
			printf("X won\n");	
		}	
		else if(f('O'))
		{
			printf("O won\n");
		}
		else if(end)
		{
			printf("Draw\n");
		}
		else
		{
			printf("Game has not completed\n");
		}
						
	}
	
	return 0;
}