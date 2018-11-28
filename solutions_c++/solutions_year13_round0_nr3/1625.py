/*
 * fairandsquare.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: stephenfebrian
 */

#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

long long numFind[100000];
int cnt;

int checkPalindrome(long long num)
{
	char str[1000];
	int start, end;
	sprintf(str,"%lld",num);
	if(strlen(str) == 1) return 1;
	if(strlen(str)%2 == 0)
	{
		start = 0;
		end = strlen(str)-1;
		while(start < end)
		{
			if(str[start] != str[end])
			{
				return 0;
			}
			start++;
			end--;
		}
		return 1;
	}
	else
	{
		start = 0;
		end = strlen(str)-1;
		while(start <= end)
		{
			if(str[start] != str[end])
			{
				return 0;
			}
			start++;
			end--;
		}
		return 1;
	}
}

void genNum(long long lim)
{
	long long i;
	for(i=1;i<= lim;i++)
	{
		long long sq = i*i;
		//if(i >= lim) printf("%lld\n",sq);
		if(0 == checkPalindrome(i))
		{
			continue;
		}
		if(0 == checkPalindrome(sq))
		{
			continue;
		}
		numFind[cnt++] = sq;
		//printf("%d\n",numFind[cnt-1]);
	}
	//printf("%lld\n",numFind[cnt-1]);
}

int main()
{
	freopen("fairandsquare.in","r",stdin);
	freopen("fairandsquare.out","w",stdout);
	int cases;
	long long start, end;
	int res;
	cnt = 0;
	//genNum(100); // small case
	genNum(10000005); // big case
	scanf("%d",&cases);
	for(int i=0;i<cases;i++)
	{
		scanf("%lld %lld",&start,&end);
		res = 0;
		for(int i=0;i<cnt;i++)
		{
			if(numFind[i] >= start && numFind[i] <= end)
			{
				res++;
			}
		}
		printf("Case #%d: %d\n",i+1,res);
	}
	fclose(stdout);
}




