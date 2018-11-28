#include <map>
#include <queue>
#include <stack>
#include <math.h>
#include <cctype>
#include <set>
#include <bitset>
#include <algorithm>
#include <list>
#include <vector>
#include <sstream>
#include <iostream>
#include <time.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> paii;


#define PI (2*acos(0))
#define ERR 1e-5
#define mem(a,b) memset(a,b,sizeof a)
#define pb push_back
#define popb pop_back
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define SZ(x) (int)x.size()
#define oo (1<<25)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define Contains(X,item)        ((X).find(item) != (X).end())
#define popc(i) (__builtin_popcount(i))
#define fs      first
#define sc      second
#define EQ(a,b)     (fabs(a-b)<ERR)
#define MAX 15050
#define wait getchar()

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t,loop=1;
    double C,F,X,last_val,now_val,ans,cnt;
    scanf("%d",&t);

    while(t--)
    {
        cnt=1.0; ans=0.0;
        scanf("%lf %lf %lf",&C,&F,&X);

        last_val=X/2.0; now_val=C/2.0 + X/(2.0+F);
        while(last_val>now_val)
        {
            ans+=C/(2.0+(cnt-1.0)*F)+1e-20;
            last_val=(X/(2.0+cnt*F));
            now_val=X/(2.0+(cnt+1.0)*F) + C/(2.0+cnt*F) ;
            cnt+=1.0;
        }
        ans+=last_val;
        printf("Case #%d: %.7lf\n",loop++,ans);

    }
    return 0;
}

