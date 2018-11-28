/*Osmos*/

#include<cstdio>
#include<algorithm>

using namespace std;

int mote[100];

int main()
{
	int A,count,i,j,N,T,temp,val;
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%d %d",&A,&N);
		for(j=0;j<N;j++)
			scanf("%d",&mote[j]);
		sort(mote,mote+N);
		count=j=0;
		if(A==1)
		{
			printf("Case #%d: %d\n",i,N);
			continue;
		}
		while(j<N)
		{
			if(mote[j]<A)
			{
				A+=mote[j];
				j++;
			}
			else
			{
				val=A;
				temp=0;
				while(val<=mote[j])
				{
					val+=val-1;
					temp++;
				}
				if(temp>=N-j)
				{
					count+=N-j;
					j=N;
				}
				else
				{
					count+=temp;
					A=val+mote[j];
					j++;
				}
			}
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}