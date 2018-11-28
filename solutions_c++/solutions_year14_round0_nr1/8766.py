#include<cstdio>
#include<iostream>
#include<algorithm>
int main()
{
	int i,j,t,k,m1[4][4],ans,m2[4][4],ans1,ans2,cnt=0,a[17];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
	    cnt=0;
	    for(j=0;j<17;j++)
            a[j]=0;
		scanf("%d",&ans1);
		for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            {
                scanf("%d",&m1[j][k]);
                if(j==ans1-1)
                    a[m1[j][k]]++;
            }
        scanf("%d",&ans2);
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            {
                scanf("%d",&m1[j][k]);
                if(j==ans2-1)
                    a[m1[j][k]]++;
            }
        for(j=1;j<17;j++)
            if(a[j]==2)
            {
                cnt++;
                ans=j;
            }
        if(cnt==0)
            printf("Case #%d: Volunteer cheated!\n",i);
        else if(cnt==1)
            printf("Case #%d: %d\n",i,ans);
        else if(cnt>=2)
            printf("Case #%d: Bad magician!\n",i);
	}
}
