#include<conio.h>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<limits>
#include<vector>
#include<bitset>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<map>
 
using namespace std;
 
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,FROM,n) for(int i=FROM;i<n;i++)
#define FORR(i,n) for(int i=n;i>=0;i--)
#define ll long long int
#define llu long long unsigned int
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slu(n) scanf("%llu",&n)
#define sf(n) scanf("%f",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define V(x) vector<x>

 
using namespace std;
 
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,FROM,n) for(int i=FROM;i<n;i++)
#define FORR(i,n) for(int i=n;i>=0;i--)
#define ll long long int
#define llu long long unsigned int
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slu(n) scanf("%llu",&n)
#define sf(n) scanf("%f",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define V(x) vector<x>
#define FILL(a,b) memset(a,b,sizeof(a))
#define max 1001
int set[max],palin[max];
int ispalindrome(int p)
{
    int temp=p,rev=0;
    while(temp>0)
    {
      rev=rev*10+temp%10;
      temp/=10;
    }
    if(rev==p)
    { palin[p]=1;
      return 1;}
    else
      //set[(p*p)]
    return 0;
}
int isperfect(int p)
{
   double temp=sqrt(p);
   int s=(int)temp;
   temp-=s;
   if(temp!=(0.0))
   return 0;
   else
   {
       if(palin[s]==1)
       return 1;
       else 
       return 0;
   }
}     
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.in","w",stdout);
    int p,test_c,a,b,count,i;
    set[1]=1;
    for(i=2;i<max;i++)
    {
         if(ispalindrome(i)&&isperfect(i))
         set[i]=1;
    }
    si(test_c);
    for(p=1;p<=test_c;p++)
    {
       count=0;
       si(a);
       si(b);
       for(i=a;i<=b;i++)
       {
          if(set[i])
          count++;
       }
       printf("Case #%d: %d\n",p,count);
    }
    getch();
    return 0;
}
