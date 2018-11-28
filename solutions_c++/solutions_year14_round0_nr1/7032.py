#include<iostream>
#include<cstdio>
#define gi(a) scanf("%d",&a);
using namespace std;
int main()
{
  int T;
  gi(T);
  for(int t=1;t<=T;t++)
  {
    int r1,r2;
    int arr1[4][4],arr2[4][4];
    gi(r1);
    for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
	gi(arr1[i][j]);
      
    gi(r2);
    for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
	gi(arr2[i][j]);
    
    r1--;
    r2--;
    int count=0,ans=-1;
    for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
      {
	if(arr1[r1][i] == arr2[r2][j])
	{
	  count++;
	  ans=arr1[r1][i];
	}
      }
    
    printf("Case #%d: ",t);
    if(count==1)
    {
      printf("%d",ans);
    }
    else if(count==0)
    {
      printf("Volunteer cheated!");
    }
    else
    {
      printf("Bad magician!");
    }
    printf("\n");
  }
}