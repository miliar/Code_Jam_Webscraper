#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <deque>
#include <stack>
#include <algorithm>
#include <climits>
#include <numeric>
#include <utility>
#include <sstream>
#include <cstring>

#define FOR(i,a,n) for(int i=a;i<n;i++)
#define FORE(i,a,n) for(int i=a;i<=n;i++)
#define REV(i,a,n) for(int i=n-1;i>=a;i--)
#define REVE(i,a,n) for(int i=n;i>=a;i--)
#define println printf("\n")
#define sortv(v) sort(v.begin(),v.end())
#define printv(i,v) FOR(i,0,v.size()) {  cout<<v[i]<<" ";}
#define printarr(i,arr,n) for(int i=0;i<n;i++) {cout<<arr[i]<<" ";}
#define scani(a) scanf("%d",&a)
#define scanc(a) scanf("%c",&a)
#define scans(a) scanf("%s",a)
#define pb push_back
#define mp(a,b) make_pair(a,b)

typedef long int LD;
typedef long long LLD;
typedef unsigned long long LLU;

using namespace std;

int main()
{
    int t;
    double c,f,x,r;
    double v1,v2,ans,pv1,pv2;
    scani(t);
    FORE(i,1,t)
     {
               r=2;ans=0.0;               
               scanf("%lf%lf%lf",&c,&f,&x);
               v1=x/r;
               v2=c/r;
               //cout<<v1<<" "<<v2<<endl;
               if(v1<=v2)
                         printf("Case #%d: %.7lf\n",i,v1);
               else
               {  
                   while(1)
                   {
                    r+=f;              
                    pv1=v1;pv2=v2;
                    v1=v2+(x/r);
                    v2=v2+(c/r);
                    if(v1>=pv1)
                    {
                              printf("Case #%d: %.7lf\n",i,pv1);
                              break;
                    }
                    //cout<<v1<<" "<<v2<<endl;i++;
                    }          
                   }
     }    
    fflush(stdin);
    getchar();
    return 0;
}
