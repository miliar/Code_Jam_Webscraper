#include<stdio.h>
#include<string.h>
#include<iostream>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
char stack[1000010];
int front;
char str[1000010];
void change()
{
	while(front >= 2 && stack[front-1] == stack[front-2])
		front-=2;
}
int main()
{
	freopen("A-large.in","r",stdin);
//	freopen("A.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		scanf("%s",str);
		int len=strlen(str);
		front=0;
		for(int i=0;i<len;i++)
		{
			stack[front++]=str[i];
			change();
		}
		int ans=len-front+front/2;
		printf("Case #%d: %d\n",cc,ans*5);
	}
	return 0;
}
/*
5
CCJJ
CJCJ
CJJC
CJJJ
CCCCCC

 */
