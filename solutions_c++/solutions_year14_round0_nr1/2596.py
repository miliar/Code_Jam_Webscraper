/* https://code.google.com/codejam/contest/2974486/dashboard
 *     Problem A. Magic Trick
 */
#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
int main()
{
    int t,l;
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        int row1,row2,i,j;
        scanf("%d",&row1);
        int a[17],b[17];
        for(i=1;i<=16;i++)
            scanf("%d",&a[i]);

        int temp1[17]={0},temp2[17]={0};
        row1--;
        for(i=row1*4+1;i<=row1*4+4;i++)
            temp1[a[i]]=1;

        scanf("%d",&row2);
        for(i=1;i<=16;i++)
            scanf("%d ",&b[i]);
        row2--;
        for(i=row2*4+1;i<=row2*4+4;i++)
            temp2[b[i]]=1;

        int count=0,num=0;
        for(i=1;i<=16;i++)
            if(temp1[i]==1 && temp2[i]==1)
                    {
                        num=i;
                        count++;
                        //printf("%d ",i);
                    }
        if(count==0)
            printf("Case #%d: Volunteer cheated!\n",l);
        if(count==1)
            printf("Case #%d: %d\n",l,num);
        if(count>1)
            printf("Case #%d: Bad magician!\n",l);

    }
    return 0;
}
