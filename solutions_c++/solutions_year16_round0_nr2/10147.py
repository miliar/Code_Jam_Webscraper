/*
Jing.alpc30
*/
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int iif = 1000000000;
const double pi = 3.1415926;
const double inf = 1e20;



int main(int argc, char *argv[])
{
	int T;
	freopen("in2.txt","r",stdin);
	freopen("ou2.txt","w",stdout);
	scanf("%d",&T);
	for(int  i = 0; i < T;i++)
	{
		char s[100];
		scanf("%s", s);
		printf("Case #%d: ",i+1);

		int ans = 0;
		int st = 0;
		int ls = strlen(s);
		for(int j = 0; j < strlen(s); j++)
		{
			if(s[ls-1-j] == '-')
			{
				if(st == 0)
					ans++;
				st = 1;
			}
			else 
			{
				if(st == 1)
					ans++;
				st = 0;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
