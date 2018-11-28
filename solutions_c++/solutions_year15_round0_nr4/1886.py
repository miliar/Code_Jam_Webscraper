#include <cmath> 
#include <cctype>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define maxn 5
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define yes jg[h][i][j]=1

bool cmp(const int a, const int b)
{
	return a > b;
}

int jg[maxn][maxn][maxn]={0};

void init()
{
	for(int h=1;h<maxn;h++)
	for(int i=1;i<maxn;i++)
	for(int j=1;j<maxn;j++)
	{
		if(i<h && j<h) continue;
		else if(h==1) yes;
		else if(h==2 && (i*j)%2==0) yes;
		else if(h==3 && i*j>=6 && (i*j)%3==0) yes;
		else if(h==4 && i*j>=12 && (i*j)%4==0) yes;
		else if(h>5 && i*j>=h*(h-1) && (i*j)%h==0) yes; 
	}
}

int main()
{
	freopen("D-small-attempt2.in","r",stdin);
	freopen("D-small-attempt2.out","w",stdout);
	int cases=0;	cin>>cases;
	init();
	int n;	string s,ans[2]={"RICHARD","GABRIEL"}; //0-NO 1-YES
	for(int _case=1;_case<=cases;_case++)
	{
		int x,r,c,f;
		scanf("%d%d%d",&x,&r,&c);
//		if(r<x && c<x) f=0;
//		else if(x==1) f=1;
//		else if(x==2) f=1-(r*c)%2;
//		else if(x==3)
//		{
//			if(r>=2 && c>=2 && (r*c)%3==0) f=1;
//			else f=0;
//		} 
//		else if(x==4)
//		{
//			if(r*c==12 || r*c==16) f==1;
//			else f=0;
//		}
		printf("Case #%d: ",_case);
		cout<<ans[jg[x][r][c]]<<endl;
	}
	return 0;
}

