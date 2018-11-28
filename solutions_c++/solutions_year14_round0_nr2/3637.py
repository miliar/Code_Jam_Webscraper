#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <climits>
#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <sstream>
#include <algorithm>
using namespace std;

#define PI acos(-1.0)
#define MAX 10000007
#define EPS 1e-9
#define mem(a,b) memset(a,b,sizeof(a))
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define FOR(i, b, e) for(int i = b; i <= e; i++)
#define pr(x) cout<<x<<"\n"
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double,double> pdd;
typedef pair<ll , ll > pll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<ll > vl;

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction


int main()
{
    //READ("A.in");
    READ("B-large.in");
    WRITE("out.out");
    int T;
    double C,F,X;
    scanf("%d",&T);
    FOR(c,1,T)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        double ck=2.0;
        double fs,ts=0.0,fr,ss;
        while(1)
        {
            fs=C/ck;
            fr=fs+(X/(ck+F));
            ss=X/ck;
            if(fr<ss)
            {
                ck+=F;
                ts+=fs;
            }
            else
            {
                ts+=ss;
                break;
            }
        }
        printf("Case #%d: %.7lf\n",c,ts);
    }
    return 0;
}


