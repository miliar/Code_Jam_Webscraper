#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <memory.h>
#include <string>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <vector>
#include <set>
#include <assert.h>

#define file_name ""

typedef long long ll;

const int N = 1e5+5;

using namespace std;

int main()
{
	// freopen(file_name".in","r",stdin);
	// freopen(file_name".out","w",stdout);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	int ans1,ans2,x;
	int a[22];
	int n = 4;
	scanf("%d",&test);
	for(int t=1;t<=test;++t)
	{
		scanf("%d",&ans1);
		memset(a,0,sizeof(a));
		for(int i=0;i<n;++i)
			for(int j=0;j<n;++j)
			{
				scanf("%d",&x);
				if (i==ans1-1)
					a[x]++;
			}
		scanf("%d",&ans2);
		for(int i=0;i<n;++i)
			for(int j=0;j<n;++j)
			{
				scanf("%d",&x);
				if (i==ans2-1)
					a[x]++;
			}

		int count = 0, id=-1;
		for(int i=0;i<20;++i)
			if (a[i]==2)
				count++, id  = i;
		printf("Case #%d: ", t);
		if (count>1)
			puts("Bad magician!");
		else if (!count)
			puts("Volunteer cheated!");
		else printf("%d\n",id);

	}
	return 0;
}
