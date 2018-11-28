#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

const int MAXN = 100000 + 10;
const int INF = 1<<30;
const double eps = 1e-8;

long long r,t;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out1","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d%d",&r,&t);
        int ans=0;
        long long rr=r+1;
        while(t>=rr*rr-r*r)
        {
      //      cout<<t<<endl;
            t-=rr*rr-r*r;
            ans++;
            rr+=2;
            r+=2;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
	return 0;
}
