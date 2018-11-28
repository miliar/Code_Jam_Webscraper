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
int t,n,cnt,res,maxm,i,tmp,ar[1004];
int main()
{
   freopen("A-large.in","r",stdin);
   freopen("opx.txt","w",stdout);
   s(t);
   while(t--)
   {
       s(n);
       s(ar[0]);
       maxm=0;
       res=0;
       cnt++;
       for(i=1;i<n;i++)
       {
           s(ar[i]);
           tmp=ar[i-1]-ar[i];
           if(tmp>0)
            res+=tmp;
           if(tmp>0 && tmp>maxm)
            maxm=tmp;
       }
       P("Case #%d: %d ",cnt,res);
       res=0;
       for(i=0;i<n-1;i++)
       {
           if(ar[i]<=maxm)
            res+=ar[i];
           else
           res+=maxm;
       }
       P("%d\n",res);
   }
}
