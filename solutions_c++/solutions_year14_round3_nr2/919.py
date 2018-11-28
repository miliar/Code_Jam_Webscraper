#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int count[256];
int order[256];
char car[256][256];
char train[1024];

bool check(char *s, int len)
{
	int last[256];
	for(int i=0;i<256;i++)
		last[i] = -1;
	int i;
	for(i=0;i<len-1;i++)
	{
		if((last[s[i]] > -1) && (
					((s[i] != s[i-1]) && (s[i] != s[i+1])) 
					|| ((i - last[s[i]]) > 1)
					)
				)
		{
				return false;
		}
		last[s[i]] = i;
	}
	if((last[s[i]] > -1) && (
				(s[i] != s[i-1]) 
				|| ((i - last[s[i]]) > 1)
				))
	{
		return false;
	}
	return true;
}
int main()
{
	int tc, i;
	int n;
	scanf("%d",&tc);
	for(int ct=1;ct<=tc;ct++)
	{
		printf("Case #%d: ",ct);
//		for(i=0;i<256;i++)
//			count[i] = 0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s", car[i]);
			order[i] = i;
//			for(int j=0;car[i][j]!='\0';j++)
//				count[car[i][j]]++;
		}
		int res;
			res = 0;
		do
		{
			sprintf(train, "\0");
			for(i=0;i<n;i++)
				strcat(train, car[order[i]]);
			if(check(train, strlen(train)))
				res++;
		}while(next_permutation(order, order+i));
		printf("%d\n",res);
	}
}
