#include <vector>
#include <iterator>
#include <algorithm>
#include <cstdio>

using namespace std;

unsigned int slevel[1001];

int main()
{
	freopen("test.in","r",stdin);freopen("result.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		int smax,sum=0,res=0;
		scanf("%d",&smax);
		//printf("smax=%d\n",smax);
		for(int i=0;i<=smax;i++) {
			scanf("%1d", &slevel[i]);
			//slevel[i]-='0';
			//printf("slevel[%d]=%d\n",i,slevel[i]);
			if(sum<i) {
				res+=i-sum;
				sum=i; 
			}
			sum+=slevel[i];
		}
		printf("%d\n", res);
		fflush(stdout);
	}
	return 0;
}
