#include<cstdio>
#include<iostream>
#include<stack>
#include<cstdlib>
#include<cstring>

using namespace std;

int map[256][256];

int fun(char ch)
{
	//printf("%c",ch);
	if(ch == 'i') return 2;
	else if(ch == 'j') return 3;
	else return 4;
}

int main()
{
	for(int i=1;i<=4;i++)
		map[i][1] = i,map[1][i] = i;
	map[2][2] = -1;map[2][3] = 4;map[2][4] = -3;
	map[3][2] = -4;map[3][3] = -1;map[3][4] = 2;
	map[4][2] = 3;map[4][3] = -2;map[4][4] = -1;
	int t;
	scanf("%d",&t);
	int cnt = 1;
	while(t--)
	{
		int l,x;
		scanf("%d %d",&l,&x);
		char str[10001],str2[10001];
		int a[10001];
		scanf("%s",str);
		str2[0] = '\0';
		for(int i=0;i<x;i++)
		{
			strcat(str2,str);
		}
		int f =2;bool flag = 0;
		//printf("%d %d\n",l,x);
		if((x*l)<3) {printf("Case #%d: NO\n",cnt++);continue;}
		//printf("%s\n",str2);
		a[0] = fun(str2[0]);
		int i;
		for(i=0;i<x*l -1;i++)
		{
			//printf("%d::%d %d\n",i,a[i],f);
			if(a[i] == f) f++,flag = 1;
			a[i+1] = fun(str2[i+1]);
			//printf("%d\n",a[i+1]);
			if(!flag)
			{
				if((a[i] >0 && a[i+1] <0 )|| (a[i] <0 && a[i+1]>0))
					a[i+1] = -1*map[abs(a[i])][abs(a[i+1])];
				else a[i+1] = map[abs(a[i])][abs(a[i+1])];
			}
			flag = 0;
		}
			//printf("\n %d %d",a[i],f);
		if((f==4 &&a[i] == 4) || (f==5 && a[i] ==1)) printf("Case #%d: YES\n",cnt++);
		else printf("Case #%d: NO\n",cnt++);
	}
	return 0;
}
