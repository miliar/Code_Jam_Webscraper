using namespace std;
#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<bitset>
#include<map>
#include<set>
#include<climits>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<cctype>
#include<queue>
#include<sstream>
#include<cassert>
#define read(x) scanf("%d",&x)
#define read2(x,y) scanf("%d%d",&x,&y)
#define read3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define write(x) printf("%d\n",x)
#define assign(x,n) x=(int*)calloc(n,4)
#define rep(i,n) for(i=1;i<=n;++i)
#define max(a,b) ((a)>(b))?(a):(b)
typedef  long long int ull;
typedef pair<int,int> pr;

int main()
{
    //freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    
    double c,f,x,ans,r;
    int t,tt=1,;
    read(t);
    while(t--)
    {
              scanf("%lf%lf%lf",&c,&f,&x);
              r=2.0;
              ans=0;
              while( c*(r+f) <x*f)
              {
                     ans+=c/r;
                     r+=f;
              }
              ans+=x/r;
              printf("Case #%d: %0.7lf\n",tt++,ans);
    }
}
