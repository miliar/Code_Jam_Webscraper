#include<stdio.h>
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cases=1,count,i,j,r,num,ans;
    
    
    
    scanf("%d",&t);
    
    int arr[17];
    while(t--)
    {
              
              for(i=0;i<=16;i++)
              arr[i] = 0;
              scanf("%d",&r);
              for(i=1;i<=4;i++)
              {
                               for(j=1;j<=4;j++)
                               {
                                                scanf("%d",&num);
                                                if(i==r)
                                                arr[num]++;
                               }
                               
                               
              }
              scanf("%d",&r);
              for(i=1;i<=4;i++)
              {
                               for(j=1;j<=4;j++)
                               {
                                                scanf("%d",&num);
                                                if(i==r)
                                                arr[num]++;
                               }
                               
                               
              }
              count = 0;
              for(i=0;i<=16;i++)
              if(arr[i]==2)
              count++,ans=i;
              
              if(count==0)
              printf("Case #%d: Volunteer cheated!\n",cases++);
              else if(count==1)
              printf("Case #%d: %d\n",cases++,ans);
              else
              printf("Case #%d: Bad magician!\n",cases++);
    }
    return 0;
}
