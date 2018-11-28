#include<stdio.h>
#include<iostream>

using namespace std;

int dui[4][2]={0,3,1,2,2,1,3,0};
char map[5][5];
string str[4];

int check()
{
	int i,f;
	int f1,f2,f3;
	for(i=0;i<4;i++)
	{
		f1=f2=f3=0;
		for(f=0;f<4;f++)
			if('X' == map[i][f])	f1++;
			else if('O' == map[i][f]) f2++;
			else f3++;
		if(f1 == 4 || (f1 == 3 && f3 ==1))
			return 0;
		if(f2 == 4 || (f2 == 3 && f3 ==1))
			return 3;
	}
	for(f=0;f<4;f++)
	{
		f1=f2=f3=0;
		for(i=0;i<4;i++)
			if('X' == map[i][f])	f1++;
			else if('O' == map[i][f]) f2++;
			else f3++;
		if(f1 == 4 || (f1 == 3 && f3 ==1))
			return 0;
		if(f2 == 4 || (f2 == 3 && f3 ==1))
			return 3;
	}
	f1=f2=f3=0;
	for(i=0;i<4;i++)
	{
		if('X' == map[i][i])	f1++;
		else if('O' == map[i][i]) f2++;
		else f3++;
	}
	if(f1 == 4 || (f1 == 3 && f3 ==1))
		return 0;
	if(f2 == 4 || (f2 == 3 && f3 ==1))
		return 3;

	f1=f2=f3=0;
	for(i=0;i<4;i++)
	{
		if('X' == map[dui[i][0]][dui[i][1]])	f1++;
		else if('O' == map[dui[i][0]][dui[i][1]]) f2++;
		else f3++;
	}
	if(f1 == 4 || (f1 == 3 && f3 ==1))
		return 0;
	if(f2 == 4 || (f2 == 3 && f3 ==1))
		return 3;
	for(i=0;i<4;i++)
		for(f=0;f<4;f++)
			if('.' == map[i][f])
				return 2;
	return 1;
}

int main()
{
	int cas,ans;
	int i,f,g;
	//freopen("D:\\A-small.in","r",stdin);
	//freopen("D:\\in.txt","w",stdout);
	str[0]="X won";
	str[1]="Draw";
	str[2]="Game has not completed";
	str[3]="O won";
	scanf("%d",&cas);
	for(i=0;i<cas;i++)
	{
		for(f=0;f<4;f++)
			scanf("%s",map[f]);
		ans=check();		
		printf("Case #%d: ",i+1);
		cout<<str[ans]<<endl;
	}
	return 0;
}