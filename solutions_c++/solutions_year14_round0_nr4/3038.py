#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int n,k,N,DeceitfulWar=0,War=0;
		double Naomi[1000],Ken[1000];
		
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			scanf("%lf",&Naomi[i]);
		for(int i=0;i<N;i++)
			scanf("%lf",&Ken[i]);
		
		sort(Naomi,Naomi+N);
		sort(Ken,Ken+N);

		n=0;
		k=0;
		while(n<N&&k<N)
			if(Naomi[n]>Ken[k])
			{
				DeceitfulWar++;
				n++;
				k++;
			}
			else
				n++;
		
		n=0;
		k=0;
		while(n<N&&k<N)
			if(Naomi[n]<Ken[k])
			{
				War++;
				n++;
				k++;
			}
			else
				k++;
		
		printf("Case #%d: %d %d\n",t,DeceitfulWar,N-War);
	}
	return 0;
}
