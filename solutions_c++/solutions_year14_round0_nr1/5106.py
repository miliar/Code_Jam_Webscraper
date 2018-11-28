#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

int A[16];
int main()
{
   // READ("A-Small.in");
    //WRITE("A-Small.out");
    int t,r1,r2;
    int B[4][4];
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {   memset(A,0,sizeof(A));
        scanf("%d",&r1);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&B[i][j]);
            }
        }
        /*for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                printf("%d ",B[i][j]);
            }
            printf("\n");

        }
        printf("\n");*/

        for(int j=0;j<4;j++)
        {
            A[B[r1-1][j]-1]++;
         //   printf("b=%d A=%d",B[])
        }
        scanf("%d",&r2);
         for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&B[i][j]);
            }
        }
        for(int j=0;j<4;j++)
        {
            A[B[r2-1][j]-1]++;
        }
        int count2=0,count22=0;
        for(int i=0;i<16;i++)
        {
            if(A[i]==2)
            {
                if(count2)
                {
                    count22=1;
                    break;
                }

                count2=i+1;

            }
        }
        if(count22>0)
        {

            printf("Case #%d: Bad magician!\n",k);
        }
        else if(count2>0)
        {
             printf("Case #%d: %d\n",k,count2);
        }
        else
             printf("Case #%d: Volunteer cheated!\n",k);
    }

}
