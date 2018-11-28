//adhoc google code jam

#include<iostream>
#include<cstdio>
#include<stdlib.h>
#include<iomanip>
#include<math.h>
#include<limits.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#define mod 1000000007
#define MAX 100000000

using namespace std;

#define PB(x) push_back(x)
#define SORT(a) sort(a.begin(),a.end())
#define INF 1000000000
#define V vector
#define S string
typedef long long LL;
typedef long double LD;
typedef long L;
typedef pair<int, int> p;
const double pi=acos(-1.0);
int main()
{
  int t,c=1;
  scanf("%d",&t);
  while(t--)
  {
    int flag[17],x,arr[5][5],cnt2=0,ans;
    memset(flag,0,sizeof(flag));
    memset(arr,0,sizeof(arr));
    for(int k=0;k<2;k++)
    {
      scanf("%d",&x);
      for(int i=1;i<=4;i++)
      {
        for(int j=1;j<=4;j++)
        {
           scanf("%d",&arr[i][j]);
           if(i==x)
           {
             flag[arr[i][j]]++;        
           }     
        }        
      }
    }  
    for(int i=1;i<=16;i++)
    {
      if(flag[i]==2)
      {
        cnt2++;
        ans=i;              
      }        
    } 
    if(cnt2==1)
    {
      printf("Case #%d: %d\n",c++,ans);           
    }       
    else if(cnt2>1)
    {
      printf("Case #%d: Bad magician!\n",c++);     
    }
    else if(cnt2==0)
    {
      printf("Case #%d: Volunteer cheated!\n",c++);    
    }
  } 
  return 0;   
}
