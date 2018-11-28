#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;
#define MAX 109
char s[MAX];
int n;
bool Com(char c)
{
	return (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u');
}

bool Csc(char s[],int begin,int n)
{
	for(int i = 0; i < n; ++i)
	{
		if(s[begin + i] == '\0')
		    return 0;
		if(!Com(*(s + begin + i)))
		    return 0;
	}
	return 1;
}

int main()
{
	int t,re = 0,left = 0,right = 0,cleft,cright,i,j,k;
	bool flag = 0;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int cas = 1; cas <= t; ++cas)
	{
		re = 0;
		flag = 0;
		cleft = -1,cright = 0;
		memset(s,0,sizeof(s));
		scanf("%s %d",s,&n);
		int slen = strlen(s);
		char *st = s;
		left = -1,right = slen;
		for(i = 0;i < slen; ++i)
		{
			if(Csc(st,i,n))
			{
				left = i;
				right = i + n - 1;
				re += (left - cleft) * (slen - right);
				cleft = left,cright = right;
			}
		}
		printf("Case #%d: %d\n",cas,re);
	}
	//system("pause");
	return 0;
}
