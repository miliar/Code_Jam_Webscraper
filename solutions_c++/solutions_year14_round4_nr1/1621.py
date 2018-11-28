#include <cstdio>
#include <algorithm>
using namespace std;

int s[10000+10];

int main()
{
	int T,casenum,N,X;
	scanf("%d",&T);
	for(casenum=1;casenum<=T;casenum++)
	{
		printf("Case #%d: ",casenum);
		scanf("%d%d",&N,&X);
		for(int i=0;i<N;i++)
			scanf("%d",s+i);
		sort(s,s+N);
		int r=N-1,ans=0;
		while(r>=0)
		{
			int l=-1;
			for(int i=0;i<r;i++)
				if(s[i]>0 && s[i]+s[r]<=X)
					l=i;
			if(l!=-1 && s[l]+s[r]<=X)
				s[l]=0;
			r--;
			while(r>=0 && s[r]==0)
				r--;
			ans++;
		}
		printf("%d\n",ans);
	}
	return 0;
}
