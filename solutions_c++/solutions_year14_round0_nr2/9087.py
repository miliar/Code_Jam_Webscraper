#include <iostream>
#include <cmath>
#include <algorithm>
#include <limits>
#include <bitset>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <time.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
using namespace std;
#define MOD 1000000007LL
#define LL long long
#define ULL unsigned long long
#define LD long double
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(x) ((x)<0?-(x):(x))
#define si(n) scanf("%d",&n)
#define sf(n) scanf("%f",&n)
#define sl(n) scanf("%lld",&n)
#define slu(n) scanf("%llu",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define pnl printf("\n")
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORR(i,n) for(int i=(n);i>=0;i--)
#define DB(x) cout<<"\n"<<#x<<" = "<<(x)<<"\n";
#define CL(a,b) memset(a,b,sizeof(a))
#define GOLD ((1+sqrt(5))/2)
const double PI=3.14159265358979323846264338327950288419716939937510582097494459230;

void preprocess()
{
}//end prepreprocess
void compute()
{
}//end compute
int main()
{

    //freopen("A.txt","r",stdin);freopen("SampleOut.out","w",stdout);
    //	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
    //	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
    //	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
    	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);

    preprocess();
    int testcase;
    scanf("%d",&testcase);
    for (int caseId=1; caseId<=testcase; caseId++)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double result=0;
        double cur_rate=2;
        bool done=false;

        while(!done)
        {
            double time1,time2;
            time1=x/(cur_rate);
            time2=c/(cur_rate) + x/(cur_rate+f);
            if(time2<time1)
            {
                result=result+ c/(cur_rate);
                cur_rate=cur_rate+f;
            }
            else
            {
                result=result+time1;
                done=true;
            }
        }
        printf("Case #%d: ",caseId);
        printf("%.7lf\n",result);
    }
    return 0;
}
