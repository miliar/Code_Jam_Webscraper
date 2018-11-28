#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <string.h>
using namespace std;

// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fillarr(a,v)                memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair

int main() {
   int t;
   s(t);
   
   forall(k,1,t+1)
   {
   
   double c,f,x,secs,rate;
   cin>>c>>f>>x;
   secs = 0;
   rate = 2;
   while(true)
   {
   double timeForFarm = c/rate;
   double currentRateTime = x/rate;
   double laterRate = rate + f;
   double laterRateTime = timeForFarm + x/laterRate;
   if(currentRateTime <= laterRateTime)
      {
      secs+=currentRateTime;
      break;
      } 
      else
      {
      rate = laterRate;
      secs+=timeForFarm;
      }

   }
   
   
   cout<<"Case #"<<k<<":"<<" ";
   printf("%.7f\n",secs);
   }
}
