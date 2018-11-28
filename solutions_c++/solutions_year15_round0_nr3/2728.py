#include<string>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<vector>
#include<iostream>
#include<deque>
#include<queue>
#include<stack>
#include<set>
#include<ctime>
#define LL __int64
#define eps 1e-8
#define zero(x) ((x > +eps) - (x < -eps))
#define mem(a,b) memset(a,b,sizeof(a))
#define MOD 1000000007
#define INF 99999999
#define MAX 100010
using namespace std;

char str[100010];
char s[3] = "ik";

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t, n, x;
	scanf("%d",&t);
	for(int ii = 1; ii <= t; ii ++)
	{
		scanf("%d%d%s",&n,&x,str);
		for(int i = 1; i < x; i ++)
		{
			for(int j = 0; j < n; j ++)
			{
				str[i*n+j] = str[j];
			}
		}
		int len = n * x;
		char ch = '1';
		int flag = 0, cnt = 0;
		for(int i = 0; i < len; i ++)
		{
			if(ch == '1')
			{
				if(str[i] == 'i')
				{
					ch = 'i';
				}
				else if(str[i] == 'j')
				{
					ch = 'j';
				}
				else
				{
					ch = 'k';
				}
			}
			else if(ch == 'i')
			{
				if(str[i] == 'i')
				{
					ch = '1';
					flag ^= 1;
				}
				else if(str[i] == 'j')
				{
					ch = 'k';
				}
				else
				{
					ch = 'j';
					flag ^= 1;
				}
			}
			else if(ch == 'j')
			{
				if(str[i] == 'i')
				{
					ch = 'k';
					flag ^= 1;
				}
				else if(str[i] == 'j')
				{
					ch = '1';
					flag ^= 1;
				}
				else
				{
					ch = 'i';
				}
			}
			else
			{
				if(str[i] == 'i')
				{
					ch = 'j';
				}
				else if(str[i] == 'j')
				{
					ch = 'i';
					flag ^= 1;
				}
				else
				{
					ch = '1';
					flag ^= 1;
				}
			}
			if(!flag)
			{
				if(cnt < 2 && ch == s[cnt])
				{
					cnt ++;
				}
			}
		}
		if(cnt == 2 && flag && ch == '1')
		{
			cnt ++;
		}
		if(cnt == 3)
		{
			printf("Case #%d: YES\n",ii);
		}
		else
		{
			printf("Case #%d: NO\n",ii);
		}
	}
	return 0;
}