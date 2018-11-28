#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int main()
{
	int k,a1,a2,a[4][4],b[4][4],j,t,i,cnt,val;
	scanf("%d",&t);
	k=1;
	while(t--)
	{
	    scanf("%d",&a1);a1--;
	    for(i=0;i<4;i++)
	    for(j=0;j<4;j++)
	    scanf("%d",&a[i][j]);

		scanf("%d",&a2);a2--;
	    for(i=0;i<4;i++)
	    for(j=0;j<4;j++)
	    scanf("%d",&b[i][j]);
	    cnt=0;

	    for(i=0;i<4;i++)
	    {
	        for(j=0;j<4;j++)
	        {
	           // cout<<a[a1][i]<<" "<<b[a2][j]<<"\n";
	            if(a[a1][i]==b[a2][j])
	           {
                cnt++;
	            if(cnt==1)
	            val=a[a1][i];
	            if(cnt>1)
	            val=-1;
	           }
	        }
	    }

	    if(cnt==0)
	    printf("Case #%d: Volunteer cheated!\n",k);
	    else
	    {
        if(val==-1)
	    printf("Case #%d: Bad magician!\n",k);
	    else
        printf("Case #%d: %d\n",k,val);
	    }

	    k++;



	}
return 0;
}
