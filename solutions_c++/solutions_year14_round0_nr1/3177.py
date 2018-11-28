#include<stdio.h>
#include<math.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<map>
#include<set>
#include<cstring>
#include<algorithm>
#define LL long long
#define N 11
#define M 121
#define println() printf("\n")
#define scani(t) scanf("%d",&t)
#define scanl(t) scanf("%lld",&t)
#define printi(t) printf("%d",t)
#define printl(t) printf("%lld",t)
using namespace std;
int main()
{int arr[4][4],sol[4];  
int t=1,ans,p,res,match;
#ifndef ONLINE_JUDGE
freopen("input.txt","r",stdin);
freopen("re.txt","w",stdout);
#endif

scani(p);
while(t<=p)
{
scani(ans);          
for(int i=0;i<4;++i)
{
for(int j=0;j<4;++j)
{scani(arr[i][j]);
if(i==ans-1)
sol[j]=arr[i][j];        
}}   
scani(ans);
for(int i=0;i<4;++i)
{
for(int j=0;j<4;++j)
{scani(arr[i][j]);
}
}       
 match=0;         
for(int j=0;j<4;++j)
{
for(int k=0;k<4;++k)
{
if(sol[k]==arr[ans-1][j])
{match++; res=sol[k];break;}       
}        
        
}        
if(match==0)
{
printf("Case #%d: Volunteer cheated!\n",t);            
}
else if(match==1)
printf("Case #%d: %d\n",t,res);
else
printf("Case #%d: Bad magician!\n",t);

t++;  
          
}

return 0;    
}
