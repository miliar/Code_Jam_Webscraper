             /*
     shubham_1286(shubham verma)
                                   */
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<vector>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<list>
#include<deque>
#include<bitset>
#include<limits.h>
#include<sstream>
#define max(x,y) x>y?x:y
#define min(x,y) x<y?x:y
#define sd(a)  scanf("%d",&a);
#define slld(a)  scanf("%lld",&a);
#define sllu(a)  scanf("%llu",&a);
#define pd(a)  printf("%d\n",a);
#define plld(a)  printf("%lld\n",a);
#define pllu(a)  printf("%llu\n",a);
#define inf INT_MAX
#define low INT_MIN
#define mod 1000000009
#define ull unsigned long long
#define ll long long
using namespace std;
int arr0[10][10];
int arr1[10][10];
int main()
{
// freopen("c:\\users\\verma\\desktop\\aa2.txt","r",stdin);
  //freopen("c:\\users\\verma\\desktop\\out2.txt","w",stdout);

int t,test_case=1;
sd(t);
while(test_case<=t){
    
    int row1,row2;
    
    sd(row1);
    
    for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4;j++)
        {
            sd(arr0[i][j]);
        }
    }
    
    
     sd(row2);
    
    for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4;j++)
        {
            sd(arr1[i][j]);
        }
    }

   int coun=0,ans;
   
   for(int i=1;i<=4;i++)
   {
       int x=arr0[row1][i];
       
       for(int j=1;j<=4;j++)
       {
            if(arr1[row2][j]==x)
            {
                coun++;
                ans=x;
                break;
            }
      }
  }
   
   if(coun>1)
        printf("Case #%d: %s\n",test_case,"Bad magician!");
    else if(coun==0)
        printf("Case #%d: %s\n",test_case,"Volunteer cheated!");
        else
        printf("Case #%d: %d\n",test_case,ans);
        
        test_case++;
   
}
  //system("pause");
 }
