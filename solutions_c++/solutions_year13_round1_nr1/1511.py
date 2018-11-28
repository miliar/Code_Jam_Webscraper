#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <stack>
#include <functional>
#include <deque>
#include <queue>
#include <math.h>
#include <bitset>
#include <set>
#include <ctype.h>

#define swap(x,y) x=x+y-(y=x)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define nline printf("\n")
#define s(a) scanf("%d",&a)
#define p(a) printf("%d",a)
#define ff first
#define ss second
#define mod 1000000009

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    long long int r,p,fp,ring;
        int t;
        scanf("%d",&t);
        for(int i=0;i<t;i++)
        {
            ring=0;
            fp=0;
            scanf("%lld %lld",&r,&p);
            while(p>=fp)
            {
                 fp+=(r+1)*(r+1)-(r*r);
                 if(fp<=p)
                    ring++;
                 r=r+2;
            }
            printf("Case #%d: %lld\n",i+1,ring);
     }
return 0;
}
