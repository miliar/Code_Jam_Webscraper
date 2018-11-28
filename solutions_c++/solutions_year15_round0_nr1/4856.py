#include <stdio.h>
#include <algorithm>
using namespace std;



int shy[1004];
char buf[1004];
int main()
{
	//freopen("A-large.in", "rt", stdin);
	//freopen("Al.out", "wt", stdout);

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t)
	{
		int Smax;
		scanf("%d%s",&Smax,buf);
		for(int s=0;s<=Smax;++s)
			shy[s]=buf[s]-'0';

		int stood=shy[0];
		int invite=0;
		for(int s=1;s<=Smax;++s)
		if(shy[s]>0)
		{
			int need=max(s-stood,0);
			invite+=need;
			stood+=need+shy[s];
		}
		
		printf("Case #%d: %d\n",t,invite);
	}

	return 0;
}