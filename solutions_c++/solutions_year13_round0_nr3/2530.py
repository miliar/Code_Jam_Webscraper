#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<stack>
#include<bitset>
#include<sstream>
#include<algorithm>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
using namespace std;
#define S(n) scanf("%d",&n)
#define SL(n) scanf("%lld",&n)
#define SS(n) scanf("%s",&n)
#define FOR(i,n) for(i=0;i<n;i++)
#define REP(i,j,n) for(i=j;i<n;i++)
typedef long long int LL;
#define MAX 10000001
LL q[10000001],temp[100],res[100];

bool check(LL n)
{
     LL l,r;
     string s;
     stringstream convert; 
     convert<<n;
     s=convert.str();
     l=0,r=s.size()-1;
     while(l<=r)
     {
               if(s[l]!=s[r])
               break;
               l++,r--;
     }
     if(l>r) 
     return true;
     else
     return false;
}

void preprocess()
{
     LL x,i=1,j=0,sz=0,idx=0;
     while(i<MAX)
     {
            q[j++]=i*i;
            i++;
     }
     FOR(i,j)
     {
             bool no=false;
             no=check(q[i]);
             if(no)
             temp[sz++]=q[i];
     }
     FOR(i,sz)
     {
              bool sq=false;
              x=(LL)sqrt(temp[i]);
              sq=check(x);
              if(sq)
              res[idx++]=temp[i];
     }
}

int main()
{
    freopen("Codejam_C_in.txt","r",stdin);
    freopen("Codejam_C_out.txt","w",stdout);
    preprocess();
    LL t,a,b,x,i,cas=1;
    SL(t);
    while(t--)
    {
              LL i=0,ans=0;
              SL(a);SL(b);
              while(res[i]<a && i<39)
              { i++; }
              while(res[i]<=b && i<39)
              {   ans++,i++; }
              printf("Case #%lld: %lld\n",cas,ans);
              cas++;
    }
    return 0;
}
