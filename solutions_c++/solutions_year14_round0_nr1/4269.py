#include<stdio.h>
using namespace std;

int main(){
	int a[17],t,a1,a2,i,j,cnt[17],count,which,d,k;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		for(i=1;i<=16;i++)
			cnt[i]=0;
		count=0;
		scanf("%d",&a1);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				scanf("%d",&d);
				if(a1==i)
					cnt[d]++;
			}
		}
		scanf("%d",&a2);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				scanf("%d",&d);
				if(a2==i)
					cnt[d]++;
			}
		}
		for(i=1;i<=16;i++)
			if(cnt[i]==2)
			{
				count++;
				which=i;
			}
		if(count>1)
			printf("Case #%d: Bad magician!\n",k);
		else if(count==0)
			printf("Case #%d: Volunteer cheated!\n",k);
		else	
			printf("Case #%d: %d\n",k,which);
	}
}
