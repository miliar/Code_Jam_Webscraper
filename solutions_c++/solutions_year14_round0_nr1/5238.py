#include<bits/stdc++.h>
using namespace std;

int pic[16][16],pic2[16][16];

int main()
{
    int ans,at,T,casen,row1,row2,i,j;
	scanf("%d",&T);
	for(casen=0;casen<T;casen++)
	{
	    ans=0;
		at=0;
	    scanf("%d",&row1);
		for(i=0;i<4;i++)
		    for(j=0;j<4;j++)
			    scanf("%d",&pic[i][j]);
		scanf("%d",&row2);
		for(i=0;i<4;i++)
		    for(j=0;j<4;j++)
			    scanf("%d",&pic2[i][j]);
	    for(i=0;i<4;i++)
		    for(j=0;j<4;j++)
			    if(pic[row1-1][i]==pic2[row2-1][j])
				{
				    at++;
					ans=pic[row1-1][i];
			    }
	    if(at==1)
		    printf("Case #%d: %d\n",casen+1,ans);
		else if(at==0)
		    printf("Case #%d: Volunteer cheated!\n",casen+1);
		else
		    printf("Case #%d: Bad magician!\n",casen+1);
	}
    return 0;
}