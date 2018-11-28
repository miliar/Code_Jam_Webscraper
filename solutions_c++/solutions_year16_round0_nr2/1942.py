#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
typedef long long LL;
char ch[10000];
int n,cnt,o;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("ans_b_large.out","w",stdout);
	cin>>cnt;
	for(int e=1;e<=cnt;e++)
	{
		o=0;
		scanf("%s",ch);
		int n = strlen(ch);
		if(ch[n-1]=='-') o=1;
		for(int i=0;i<n-1;i++)
			if(ch[i] != ch[i+1]) o++;
		printf("Case #%d: %d\n",e,o);
	}
}
