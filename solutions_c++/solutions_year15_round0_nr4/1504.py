#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#define s(n) scanf(" %d",&n)
#define ss(n) scanf(" %s",n)
#define s2(a,b) scanf(" %d %d",&a,&b)
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
int t,x,r,c,cnt;
int main()
{
   freopen("D-small.in","r",stdin);
   freopen("opx.txt","w",stdout);
   s(t);
   while(t--)
   {
   s(x);
   s2(r,c);
   cnt++;
   if(x==1)
   P("Case #%d: GABRIEL\n",cnt);
   else if(x==2)
   {
      if((r&1)==0 || (c&1)==0)
      P("Case #%d: GABRIEL\n",cnt);
      else
      P("Case #%d: RICHARD\n",cnt);
   }
   else if(x==3)
   {
       if((r==3 && c==1) || (r==1 && c==3))
       P("Case #%d: RICHARD\n",cnt);
       else if((r*c)%3==0)
       P("Case #%d: GABRIEL\n",cnt);
       else
       P("Case #%d: RICHARD\n",cnt);
   }
   else
   {
       if(r!=4 && c!=4)
       P("Case #%d: RICHARD\n",cnt);
       else if((r==4 && c==1) || (r==1 && c==4))
       P("Case #%d: RICHARD\n",cnt);
       else if((r==4 && c==2) || (r==2 && c==4))
       P("Case #%d: RICHARD\n",cnt);
       else if((r==4 && c==3) || (r==3 && c==4))
       P("Case #%d: GABRIEL\n",cnt);
       else if((r==4 && c==4) || (r==4 && c==4))
       P("Case #%d: GABRIEL\n",cnt);
   }
   }
   return 0;
}
