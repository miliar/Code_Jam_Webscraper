#include<iostream>
#include<conio.h>
#include<stdio.h>
using namespace std;
int main()
{
    freopen("C:\\Users\\ARNAB BANERJEE\\google\\qns.txt","r",stdin);
    freopen("C:\\Users\\ARNAB BANERJEE\\google\\ans1.txt","w",stdout);
    int t;
    int ans1,ans2;
    scanf("%d",&t);
    int arr1[4][4];
    int arr2[4][4];  
    int case1=0;
    int i,j;
    while(t--)
    {
        case1++;
        scanf("%d",&ans1);
        for(i=0;i<4;i++)
        {
           for(j=0;j<4;j++)
           {
               scanf("%d",&arr1[i][j]);
           }
        }
        scanf("%d",&ans2);
        int cnt=0;
        int k;
        int x,y;
        int ans;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&arr2[i][j]);
                
            }
        }
        int flag=0;
        for(j=0;j<4;j++)
        {
            int s=arr1[ans1-1][j];
            for(k=0;k<4;k++)
            {
               if(arr2[ans2-1][k]==s)
               {
                   cnt++;
                   ans=s;
                   break;
               }
            }
               if(cnt>1)
               {
                  flag=1;
                  break;
               }
            
        }
        printf("Case #%d: ",case1);
        if(cnt==0)
            printf("Volunteer cheated!\n");
        else if(flag==1)
            printf("Bad magician!\n");
        else if(cnt==1)
            printf("%d\n",ans);
    }
   //getch();
    return 0;
}
               
