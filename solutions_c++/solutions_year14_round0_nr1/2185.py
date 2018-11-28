#include<bits/stdc++.h>
using namespace std;int main()
{
    freopen ("A-small-attempt0.in","r",stdin);
    freopen ("output.txt","w",stdout);
    int t,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        int a,A[4][4],b,B[4][4],i,j,count=0,e=0;
        scanf("%d",&a);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            scanf("%d",&A[i][j]);
        scanf("%d",&b);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            scanf("%d",&B[i][j]);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                if(A[a-1][i]==B[b-1][j])
                {
                    count++;
                    e=A[a-1][i];
                }

            }
        //cout<<count<<" "<<e<<endl;
        printf("Case #%d: ",k);
        if(count>1)
        {
            printf("Bad magician!\n");
        }
        else if(count==1)
        {
            printf("%d\n",e);
        }
        else
        {
            printf("Volunteer cheated!\n");

        }

    }
    fclose (stdout);
    fclose (stdin);
    return 0;
}
