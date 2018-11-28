#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <cstdlib>
#include <algorithm>
using namespace std;

char data[10000001]={};
int n;
int main()
{
	int t;
	freopen("A-small-attempt3.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&t);
	for(int i = 1; i <= t; i++)
	{
		cin>>n;
		scanf(" %s",&data);
		int count = data[0] - '0';
		int sum = 0;
		for(int j = 1; j <= n; j++)
		{
		  if(j > count)
		  {
		  	int x= j - count;
		  	count +=  x + data[j] - '0';
		  	sum += x;
		  }
		  else
		  {
		  	count += data[j]-'0';
		  }
		  if(count >= 10)
		  	break;
		}
		printf("Case #%d: %d\n",i,sum);
	}
	return 0;
}
