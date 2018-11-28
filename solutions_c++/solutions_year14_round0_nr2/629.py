/*
TASK: <Task>
LANG: C++
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<stack>
#include<bitset>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;

int N,M,T;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int tt=0;
    while(T--)
    {
        tt++;
        double C,F,X,a,b,t;
        scanf("%lf%lf%lf",&C,&F,&X);
        double Mc=0,rate=2.0;
        while(true)
        {
            a=C/rate;
            b=X/rate;
            t=a+X/(rate+F);
            if(t>b)
            {
                Mc+=b;  break;
            }
            else
                Mc+=a,rate+=F;
        }
        printf("Case #%d: %lf\n",tt,Mc);
    }
}
