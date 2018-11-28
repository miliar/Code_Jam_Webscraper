/* ***********************************************
Author        :axp
Created Time  :2015/4/11 15:00:21
File Name     :1.cpp
************************************************ */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;


const int Mut[5][5] = {
	{},
	{0,1,2,3,4},
	{0,2,-1,-4,3},
	{0,3,4,-1,-2},
	{0,4,-3,2,-1}
};

int Div[5][5];


const int maxn = 10010;
int arr[maxn];
int T;
long long n;
int l;
int num;
int kase;
int t;
bool ans;
int sta;
int B[20];
int *b = B+10;
char ch[maxn];

int work(int x,int y)
{
	swap(x,y);
	bool b=0;
	if(x<0)
	{
		b=!b;
		x=-x;
	}
	if(y<0)
	{
		b=!b;
		y=-y;
	}
	int re=Mut[x][y];
	if(b)
		re=-re;
	//cout<<x<<' '<<y<<' '<<re<<endl;
	return re;
}

void print()
{
	if(ans)
		printf("Case #%d: YES\n",kase);
	else
		printf("Case #%d: NO\n",kase);
}

int main()
{
    freopen("7","r",stdin);
    freopen("out.txt","w",stdout);

	for(int i=1;i<=4;i++)
		for(int j=1;j<=4;j++)
		{
			int t=abs(work(i,j));
			Div[t][j]=i;
		}


	scanf("%d",&T);
	for(kase=1;kase<=T;kase++)
	{
		scanf("%lld%d",&n,&l);
		//getchar();
		sta=0;
		num=1;
		ans=0;
		memset(B,0,sizeof(B));
		

		scanf("%s",ch);

		for(int i=1;i<=n;i++)
		{
			arr[i]=ch[i-1]-'g';
		}

		for(int i=1;i<l;i++)
		{
			for(int j=1;j<=n;j++)
			{
				arr[i*n+j]=arr[j];
			}
		}

		for(int i=1;i<=n*l;i++)
		{
			num=work(num,arr[i]);
			if(num==2)
			{
				sta|=1;
			}
			else if(sta && num==4)
			{
				sta|=2;
			}
		}

		if(sta==3 && num==-1)
			ans=1;

		print();
	}
    return 0;
}


