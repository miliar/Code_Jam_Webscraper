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
{   
//#ifndef ONLINE_JUDGE
freopen("input.txt","r",stdin);
freopen("res.txt","w",stdout);
//#endif
int i=1,t,n,j,p=1,count,dcount;
double A[1000],B[1000];
scani(t);
while(p<=t)
{count=dcount=0;
scani(n);           
for( j=0;j<n;++j)
scanf("%lf",&A[j]);
for( j=0;j<n;++j)
scanf("%lf",&B[j]);
sort(A,A+n);
sort(B,B+n);
j=0;i=0;
while(j<n)
{
if(B[j]>A[i])
{j++;i++;}
else
{j++;count++;}          
          
}           
j=i=0;
while(i<n)
{
if(A[i]>B[j])
{j++;dcount++;}          
 i++;         
}
           
 printf("Case #%d: %d %d\n",p,dcount,count);          
p++;}
   
    
    
return 0;    
}
