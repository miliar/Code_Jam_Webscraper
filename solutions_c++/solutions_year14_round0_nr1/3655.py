#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include<stdio.h>
void main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++)
	{
		int temp,a,b,c,d,chk[16]={0},cnt=0,ans,i;
		scanf("%d",&temp);
		for(i=0;i<temp;i++)
			scanf("%d %d %d %d",&a, &b, &c, &d);
		chk[a-1]+=1;
		chk[b-1]+=1;
		chk[c-1]+=1;
		chk[d-1]+=1;
		for(i=temp;i<4;i++)
			scanf("%d %d %d %d",&a, &b, &c, &d);
		scanf("%d",&temp);
		for(i=0;i<temp;i++)
			scanf("%d %d %d %d",&a, &b, &c, &d);
		chk[a-1]+=1;
		chk[b-1]+=1;
		chk[c-1]+=1;
		chk[d-1]+=1;
		for(i=temp;i<4;i++)
			scanf("%d %d %d %d",&a, &b, &c, &d);
		for(i=0;i<16;i++)
		{
			if(chk[i]==2)
			{
				cnt++;
				ans=i;
			}
		}
		printf("Case #%d: ",t+1);
		if(cnt==1)
			printf("%d\n",ans+1);
		else if(cnt>1)
			printf("Bad magician!\n");
		if(cnt==0)
			printf("Volunteer cheated!\n");
	}
}