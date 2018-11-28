#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    int cas=0;
    int r1,r2,a[4][4],a1[4],a2[4],i,j,cnt,p;
    while(t>0)
    {
        t-=1;cas+=1;
        scanf("%d",&r1);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        }
        for(i=0;i<4;i++)
            a1[i]=a[r1-1][i];
        scanf("%d",&r2);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        }
        for(i=0;i<4;i++)
            a2[i]=a[r2-1][i];
      //  for(i=0;i<4;i++)
        //    cout<<a1[i]<<" "<<a2[i]<<endl;
        cnt=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a1[i]==a2[j])
                    {cnt++;p=a1[i];}
            }
        }
        if(cnt==0)
            printf("Case #%d: Volunteer cheated!\n",cas);
        if(cnt==1)
            printf("Case #%d: %d\n",cas,p);
        if(cnt>1)
            printf("Case #%d: Bad magician!\n",cas);
    }
    return 0;
}
