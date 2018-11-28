#include<iostream>


using namespace std;
int main()
{
    int t,one,two,ans,count;
    int temp[17];
    int ar[4][4];
    scanf("%d",&t);
    for(int p=1;p<=t;p++)
    {
      for(int i=1;i<17;i++)
      temp[i]=0;
      count=0;
      ans=0;
      scanf("%d",&one);
      for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
      scanf("%d",&ar[i][j]);
       for(int j=0;j<4;j++)
        temp[ar[one-1][j]]=1;
      scanf("%d",&two);
      for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
      scanf("%d",&ar[i][j]);
      for(int j=0;j<4;j++)
        {if(temp[ar[two-1][j]]==1) 
        ans=ar[two-1][j];
        else
        temp[ar[two-1][j]]=1;}
      for(int i=1;i<17;i++)
        if(temp[i])
        count++;
      if(count==7)
      {printf("\nCase #%d: %d",p,ans);}
      else if(count==8)
      {printf("\nCase #%d: Volunteer cheated!",p);}
      else
      {printf("\nCase #%d: Bad magician!",p);}  
      
    }
    return 0;
}
