#include<iostream>
using namespace std;
int main()
{
    

    freopen("A-small-attempt0.in","r",stdin);
    freopen("outer.txt","w",stdout);
    
    int cases;
    
    scanf("%d",&cases);
    for(int c =1;c<=cases;c++)
    {
                  int num1,num2;
                  scanf("%d",&num1);
                  int arr[5][5];
                  int brr[5][5];
                  for(int i=1;i<=4;i++)
                  {
                          for(int j=1;j<=4;j++)
                          {
                                  scanf("%d",&arr[i][j]);
                          }
                  }
                  scanf("%d",&num2);
                  for(int i=1;i<=4;i++)
                  {
                          for(int j=1;j<=4;j++)
                          {
                                  scanf("%d",&brr[i][j]);
                          }
                  }
                  int ct =0;
                  int ans[17];
                  for(int i=0;i<=16;i++)
                  {
                          ans[i]=0;
                  }
                  for(int i=1;i<=4;i++)
                  {
                   ans[arr[num1][i]]++;
                  }
                  int number;
                  for(int i=1;i<=4;i++)
                  {
                          if(ans[brr[num2][i]]==1)
                          {
                                                  number =brr[num2][i];
                          ct++;
                          }
                  }       
                  if(ct>1)
                  {
                          printf("Case #%d: Bad magician!\n",c);
                  }
                  else if(ct==1)
                  {
                       printf("Case #%d: %d\n",c,number);
                  }
                  else if(ct==0)
                  {
                       printf("Case #%d: Volunteer cheated!\n",c);
                   }
    }
    return 0;
}  

