#include <cstdio>
#include <cstring>

using namespace std;

long v1[5],v2[5],ans1,ans2,i,j,tc,nrsol,sol;

int main () {
	
	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	
	scanf("%ld",&tc);
	
	long k=0;
	
	while(tc--)
	{
		k++;
		nrsol=0;
		scanf("%ld",&ans1);
		memset(v1,0,sizeof(v1));
		memset(v2,0,sizeof(v2));
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			{
				long temp;
				scanf("%ld",&temp);
				if(i==ans1)
					v1[j]=temp;
			}
		scanf("%ld",&ans2);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			{
				long temp;
				scanf("%ld",&temp);
				if(i==ans2)
					v2[j]=temp;
			}
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				if(v1[i]==v2[j])
				{
					nrsol++;
					sol=v1[i];
				}
		if(nrsol==1)
			printf("Case #%ld: %ld\n",k,sol);
		if(nrsol==0)
			printf("Case #%ld: Volunteer cheated!\n",k);
		if(nrsol>1)
			printf("Case #%ld: Bad magician!\n",k);
	}
	
	return 0;
}
