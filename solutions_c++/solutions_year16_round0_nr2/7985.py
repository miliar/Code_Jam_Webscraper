#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <string>
#include <time.h>

#define SQR(_x) ((_x)*(_x))
#define NL printf("\n")
#define LL long long
#define DB double
#define PB push_back
#define INF 1<<30
#define LB lower_bound
#define UB upper_bound
#define F front
#define PQ priority_queue

using namespace std;

int main()
{
	int n;
	char s[110];
	int l,count=0;
	int state=0;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		scanf("%s",s);
		l=strlen(s);
		count=0;
		for(int j=0;j<l-1;j++)
		{
			if(s[j]!=s[j+1])
			{
				count++;
			}
		}
		if(s[l-1]=='-') count++;
		printf("Case #%d: %d\n",i+1,count);
	}

	return 0;
}