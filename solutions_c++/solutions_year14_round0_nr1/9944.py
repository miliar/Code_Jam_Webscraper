#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#define FILL(v,a) memset(&v,a,sizeof(v));
using namespace std;

int main()
{
    int testcases,index,i,j,rowno1,rowno2;
    scanf("%d",&testcases);
    bool arr[17],flag;
    for(index=1;index<=testcases;index++)
    {
      FILL(arr,false);
      flag=false;
      scanf("%d",&rowno1);
      int a[4][4];
      for(i=0;i<4;i++)
      {
        if(i+1==rowno1)
         flag=true;
        for(j=0;j<4;j++)
        {
          scanf("%d",&a[i][j]);
          if(flag)
          {
            arr[a[i][j]]=true;
          }
        }
        flag=false;
      }
      scanf("%d",&rowno2);
      flag=false;
      int count=0;
      int printnum=-1;
      for(i=0;i<4;i++)
      {
        if(i+1==rowno2)
         flag=true;
        for(j=0;j<4;j++)
        {
          scanf("%d",&a[i][j]);
          if(flag)
          {
            if(arr[a[i][j]]==true)
            {
             printnum=a[i][j];
             count++;
            }
          }
        }
        flag=false;
      }
      if(count==1)
      {
        printf("Case #%d: %d\n",index,printnum);
      }
      if(count==0)
      {
        printf("Case #%d: Volunteer cheated!\n",index);
      }
      if(count>1)
      {
        printf("Case #%d: Bad magician!\n",index);
      }
    }
	return 0;
}
