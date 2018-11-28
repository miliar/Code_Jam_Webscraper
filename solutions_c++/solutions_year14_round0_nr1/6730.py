#include<stdio.h>
#include<iostream>

using namespace std;
int arr1[5][5],arr2[5][5];
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,a,b;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        int m[20]={0};
        scanf("%d",&a);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                scanf("%d",&arr1[i][j]);
                if(i==a-1)
                    m[arr1[i][j]]=1;
            }
        scanf("%d",&b);
        int ans;
        int f=0;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                scanf("%d",&arr2[i][j]);
                if(i==b-1)
                {
                    if(m[arr2[i][j]]==1)
                    {
                        if(f==0)
                        {
                            f=1;
                            ans=arr2[i][j];
                        }
                        else
                            f=2;
                    }
                }
            }
        if(f==0)
            printf("Case #%d: Volunteer cheated!\n",k);
        else if(f==1)
            printf("Case #%d: %d\n",k,ans);
        else
            printf("Case #%d: Bad magician!\n",k);
    }
    return 0;
}
