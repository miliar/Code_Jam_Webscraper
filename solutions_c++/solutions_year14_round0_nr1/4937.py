#include <stdio.h>
#define N 4



    
int main()
{
        int T;
        scanf("%d",&T);
        for(int i=0;i<T;i++)
        {
            int x,y;
            int num=0;
            int right=0;
            int a[16],b[16];
            scanf("%d",&x);
            for(int j=0;j<16;j++)
                scanf("%d",&a[j]);
            scanf("%d",&y);
            for(int j=0;j<16;j++)
                scanf("%d",&b[j]);
            for(int j=0;j<N;j++)
                for(int k=0;k<N;k++)
                if(a[N*(x-1)+j] == b [N*(y-1)+k])
                {
                    right=b [N*(y-1)+k];
                    num ++;
                }
            if(num==1)
                printf("Case #%d: %d\n",i+1,right);
            else if(num==0)
                printf("Case #%d: Volunteer cheated!\n",i+1);
            else
                printf("Case #%d: Bad magician!\n",i+1);
        }
}

