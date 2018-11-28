#include <iostream>
#include <fstream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <cmath>
#include <math.h>
#include <stdlib.h>

#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
using namespace std;
int main()
{
	int T;
	int N;
	double a[1001],b[1001];
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		scanf("%d",&N);
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for (int j=0;j<N;j++)
			scanf("%lf",&a[j]);
		for (int j=0;j<N;j++)
			scanf("%lf",&b[j]);
		sort(a,a+N);
		sort(b,b+N);
		int cnt_b_win = 0;
		int p = 0;
		for (int j=0;j<N;j++)
		{
			while(b[p]<a[j] && p < N)
				p++;
			if (p==N)
				break;
			else cnt_b_win ++;
			p++;
		}
		int z = N - cnt_b_win;
		
		int cnt_a_win = 0;
		p = 0;
		for (int j=0;j<N;j++)
		{
			while(a[p]<b[j] && p < N)
				p++;
			if (p==N)
				break;
			else cnt_a_win ++;
			p++;
		}
		int y = cnt_a_win;
		printf("Case #%d: %d %d\n",i, y, z);

	}
	return 0;
}