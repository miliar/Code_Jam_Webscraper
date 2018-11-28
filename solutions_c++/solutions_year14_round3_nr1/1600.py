//Eklavya Abinash Abhi (Om)
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <climits>
#include <iostream>
#include <iomanip>
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
#define lcm(a,b) (a*(b/gcd(a,b)))
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define Sort(x) sort(x.begin(),x.end())
#define Reverse(x) reverse(x.begin(),x.end())
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

using namespace std;

long long gcd(long long a,long  long b) {
  return b == 0 ? a : gcd(b, a % b);
}

int main()
{
    READ("A-large.in");
    WRITE("out.out");
    int T;
    long long a,b;
    scanf("%d",&T);

    FOR(i,1,T)
    {
        scanf("%lld/%lld",&a,&b);
        long long g=gcd(a,b);
        a=a/g;
        b=b/g;
        long long c=b,d;
        int p=log2(a);
        int q=log2(b)+EPS;
        double r=log2(b)+0.0000000001;
        if(a<b&&r-q<EPS)
        {
            int ans=q-p;
            printf("Case #%d: %d\n",i,ans);
        }
        else
           printf("Case #%d: impossible\n",i);
    }
    return 0;
}

