#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <list>
#include <vector>
using namespace std;
int gs(char a,char b,char c,char d)
{
	char s[4]={a,b,c,d};
	int s1=0,s2=0,s3=0;
	for(int i=0;i<4;i++)
	{
		if(s[i]=='.')return 2;
		if(s[i]=='O')s1++;
		else if(s[i]=='X')s2++;
		else s3++;
	}
	if(s1==4||(s1==3&&s3))return 0;
	if(s2==4||(s2==3&&s3))return 1;
	return 3;

}
int main()
{
	int tes,cas=1;
	//freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>tes;
	char mat[33][44];
	while(tes--)
	{
		//cout<<tes<<endl;
		int fk=0;
		for(int i=0;i<4;i++)
			for(int q=0;q<4;q++)
				cin>>mat[i][q];
		int da[3]={0};
			da[gs(mat[0][0],mat[1][1],mat[2][2],mat[3][3])]++;
			da[gs(mat[3][0],mat[2][1],mat[1][2],mat[0][3])]++;
		for(int i=0;i<4;i++)
		{
			da[gs(mat[i][0],mat[i][1],mat[i][2],mat[i][3])]++;
			da[gs(mat[0][i],mat[1][i],mat[2][i],mat[3][i])]++;
		}
		printf("Case #%d: ",cas++);
		if(da[0]==1&&da[1]==0)puts("O won");
		else if(da[0]==0&&da[1]==1)puts("X won");
		else if(da[2])puts("Game has not completed");
		else puts("Draw");
	}

}