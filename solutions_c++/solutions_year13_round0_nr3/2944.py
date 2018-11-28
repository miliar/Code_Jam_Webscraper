#include<stdio.h>
int main()
{
    int data[5] = {1,4,9,121,484};
    int t,a,b,count=0;
  //  freopen("in.txt","r",stdin);
  //  freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        count=0;
        scanf("%d %d",&a,&b);
        for(int j=0;j<5;j++)
        {
            if(data[j]>=a && data[j]<=b)
                count++;
        }    
        printf("Case #%d: %d\n",i+1,count);
    }    
    return 0;
}    
