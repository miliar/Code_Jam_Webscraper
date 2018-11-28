#include<cstdio>
using namespace std;

int main()
{
//	freopen("input.txt","r",stdin);
	int i,j,k,t,ans1,ans2,arr1[4],arr2[4],count,y;

	scanf("%d",&t);

	for(i=1;i<=t;i++)
	{
	    scanf("%d",&ans1);
	    ans1--;
	    for(j=0;j<ans1;j++)
        {
            for(k=0;k<4;k++)
                scanf("%*d");   //asterisk suppresses assignment of specifier. Scanf will read the variable but not store it.
        }

        for(;j<=ans1;j++)
        {
            for(k=0;k<4;k++)
                scanf("%d",&arr1[k]);
        }

        for(;j<4;j++)
        {
            for(k=0;k<4;k++)
                scanf("%*d");
        }

        scanf("%d",&ans2);
        ans2--;
        for(j=0;j<ans2;j++)
        {
            for(k=0;k<4;k++)
                scanf("%*d");
        }

        for(;j<=ans2;j++)
        {
            for(k=0;k<4;k++)
                scanf("%d",&arr2[k]);
        }

        for(;j<4;j++)
        {
            for(k=0;k<4;k++)
                scanf("%*d");
        }

//        for(j=0;j<4;j++)
//            printf("%2d ",arr1[j]);
//        printf("\n");
//        for(j=0;j<4;j++)
//            printf("%2d ",arr2[j]);
//        printf("\n");

        count = 0;
        y = 0;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                if(arr1[j] == arr2[k])
                {
                    count++;
                    y = arr1[j];
                }
            }
        }

        printf("Case #%d: ",i);
        if(count == 0)
            printf("Volunteer cheated!\n");
        else if(count > 1)
            printf("Bad magician!\n");
        else if(count == 1)
            printf("%d\n",y);

	}
	return(0);
}
