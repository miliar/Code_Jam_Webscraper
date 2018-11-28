#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#define s(n) scanf("%d",&n)
#define ss(n) scanf(" %s",n)
#define s2(a,b) scanf("%d %d",&a,&b)
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define ii pair<int,int>
#define F first
#define S second
#define P printf
#define E <<endl
#define mid (st+(end-st)/2)
using namespace std;
int t,n,i,sum,res,cnt;
char str[1004];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("op1.txt","w",stdout);
    s(t);
    while(t--)
    {
       s(n);
       ss(str);
       res=0;
       sum=str[0]-48;
       for(i=1;i<=n;i++)
       {
          if(i>sum)
          {
            res+=(i-sum);
            sum+=(i-sum+str[i]-48);
          }
          else
          sum+=(str[i]-48);
       }
       cnt++;
       P("Case #%d: %d\n",cnt,res);
    }
    return 0;
}
