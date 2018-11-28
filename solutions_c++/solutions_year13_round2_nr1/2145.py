#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>
#include <cmath>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	int E,R,N,A,ans;
	int s[1001];
	int l[1001],r[1001],sl[1001],sr[1001];
	scanf("%d",&T);
	for (int cs=1;cs<=T;cs++)
	{
		scanf("%d%d",&A,&N);
		for (int i=0;i<N;i++)
		{
			scanf("%d",s+i);
		}
		if (A==1)
			printf("Case #%d: %d\n",cs,N);
		else
		{
			sort(s,s+N);
			int start = A;
			int cntl = 1,cntr = 0,cnti = 0;
			l[0]=0;
			//cout<<l[0]<<endl;
			while(cnti<N)
			{
				int cnt = 0;
				while(cnti< N && s[cnti]<start)
				{
					start = start + s[cnti];
					cnti++;
					cnt++;
				}
				r[cntr] = cnt;
				cntr++;
				if (cnti==N)
					break;
				cnt = 0;
				while(cnti< N && start <= s[cnti])
				{
					start += start-1;
					cnt++;
				}
				l[cntl]=cnt;
				cntl++;
			}
			sl[0]=l[0];
			sr[0]=r[0];
			for (int i=1;i<cntl;i++)
			{
				sl[i]=sl[i-1]+l[i];
				sr[i]=sr[i-1]+r[i];
			}
			for (int i=0;i<cntr;i++)
			{
				sr[i] = N - sr[i];
			}
			int ans = N+10000000;
			for (int i=0;i<cntl;i++)
			{
				if (sl[i]+sr[i]<ans)
					ans = sl[i]+sr[i];
			}
			printf("Case #%d: %d\n",cs,ans);
		}
	}
	return 0;
}