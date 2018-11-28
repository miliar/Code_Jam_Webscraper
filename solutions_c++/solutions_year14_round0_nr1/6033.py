#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;
int mmap1[5][5];
int mmap2[5][5];
int n,m;
int main()
{
    int t,i,j,num[1000],k=1;
    freopen("A-small-attempt4.in","r",stdin);
    freopen("12.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        memset(mmap1,0,sizeof(mmap1));
        memset(mmap2,0,sizeof(mmap2));
        memset(num,0,sizeof(num));
        scanf("%d",&n);
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
                scanf("%d",&mmap1[i][j]);
        scanf("%d",&m);
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
                scanf("%d",&mmap2[i][j]);
        int cnt=0;
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
            {
                if(mmap1[n-1][i]==mmap2[m-1][j])
                    num[cnt++]=mmap1[n-1][i];
            }
        // printf("%d\n",cnt);
        if(cnt==0)
            printf("Case #%d: Volunteer cheated!\n",k++);
        else if(cnt==1)
            printf("Case #%d: %d\n",k++,num[0]);
        else if(cnt>1)
            printf("Case #%d: Bad magician!\n",k++);
    }
    return 0;
}
