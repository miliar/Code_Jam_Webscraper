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

    //	freopen("A.in","r",stdin);freopen("SampleOut.out","w",stdout);
    	freopen("A-small-attempt1.in","r",stdin);
    	freopen("A-small-attempt1.out","w",stdout);
    //	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
    	//freopen("input.in.txt","r",stdin);freopen("A-small-attempt2.out","w",stdout);
    preprocess();
    int testcase;
    scanf("%d",&testcase);
    int A[5][5];
    for (int caseId=1; caseId<=testcase; caseId++)
    {
        int a;
        int first[4];
        int second[4];
        scanf("%d",&a);
        for(int i=0;i<4;i++)
                for(int j=0;j<4;j++)
                    scanf("%d",&A[i][j]);
        a--;
        for(int i=0;i<4;i++)
            first[i]=A[a][i];

        scanf("%d",&a);
        for(int i=0;i<4;i++)
                for(int j=0;j<4;j++)
                    scanf("%d",&A[i][j]);
        a--;
        for(int i=0;i<4;i++)
            second[i]=A[a][i];


        vector<int> v(10);
        vector<int>::iterator it;

        sort(first,first+4);
        sort(second,second+4);

        it=set_intersection (first, first+4, second, second+4, v.begin());
        v.resize(it-v.begin());
        printf("Case #%d: ",caseId);
        if(v.size()>1)
            printf("Bad magician!\n");
        else if(v.size()==0)
            printf("Volunteer cheated!\n");
        else
            printf("%d\n",v.at(0));
    }

    return 0;
}
