/*
    shubham_1286
   algo =             */
using namespace std;
#include<cassert>
#include<cctype>
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
#include<sstream>
#include<algorithm>
#include<list>
#include<deque>
#include<bitset>
#include<limits>
#include<sstream>
#define max(x,y) x>y?x:y
#define min(x,y) x<y?x:y
#define inf INT_MAX
#define low INT_MIN
#define mod 1000000007
int palin( int x, int count)
{ 
 int a[10],i=0;
 for(i=0;x!=0;i++)
  {   
   a[i]=x%10;
   x=x/10;
   count++;  
  }
 int flag;
int p=count;
for(i=0;i<(p+1)/2;i++)
{
   flag=1;                   
  //int w=count-1;    
  count--;
 if(a[i]!=a[count]) 
    {flag=0;      
   break;}
  // cout<<p<<count<<"\n";
 }
// cout<<flag<<"\n";
if(flag==1) 
return 1; 
else
return 0;
}  
int main()
{
int t;
scanf("%d",&t);
int test=1;
while(test<=t)
{
int l,f,moun=0,r,a=10,b=10;
scanf("%d%d",&l,&f);
while(l<=f)
{
int m=l;
double p=sqrt(l);
if(p==(int)p)
{r=0;}
else
r=1;
if(r==0)
{
 a=palin(l,0);
 b=palin(int(p),0);
// cout<<a<<"  "<<b<<endl;
 if(a==1&&b==1)
moun++;
}

l++;
}
printf("case #%d: %d\n",test,moun);
test++;
}
}
