#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <queue>
#include <ctime>
#include <fstream>
#include <sstream>
#include <cmath>
#include <limits.h>
#include <cstdlib>
#include <stack>


#define abs(x) ((x)>=0? (x):(-x))
#define gc getchar_unlocked
#define s(x) scanf("%d",&x)
#define sil(x) scanf("%llu",&x)
#define sd(x) scanf("%ld",&x)
#define in(s) cin>>s
#define FOR(a) for( int i= 0 ; i<(a); ++i) // exclusive for
#define FORR(a) for( int i=(a-1) ; i>=(0); --i)
#define REP(a) for(int k=0; k <= (a); ++k) // inclusive for
#define REPR(a) for( int i=(a) ; i>=(0); --i)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define SZ(x) ((int)((x).size()))
#define SRT(v) std::sort(ALL(v))
#define CTN(x) std::cout<<x<<'\n' //cout with newline
#define CTS(x) std::cout<<x<<" " //cout with space
#define CT(x) std::cout<<x
#define CLR(x) std::memset(x,0,sizeof(x))
#define FILL(x,n) std::fill_n(x,sizeof(x),n)
#define T(t) int t=read<int>();// while(t--)
#define DBGA(x,n) {for(int i=0;i<n;i++) cout<<x[i]<<" "; cout<<"\n";}
#define REC(x) clock_t x=clock()
#define CPS CLOCKS_PER_SEC
#define TM(x,y) CTN(((double)(y-x)/CPS));


typedef std::vector<int> VI;
typedef std::vector<long long int> VL;
typedef std::vector<unsigned long long int> VULL;
typedef std::vector<std::string> VS;
typedef std::map<int,int> MI;
typedef std::pair<int,int> PII;
typedef std::string str;
typedef unsigned long long ull;
typedef long long ll;
typedef long int li;


using namespace std;

char smax[1010];
int main()
{
    int t;
    int s,sum=0,ans=0;
    cin>>t;
    for(int j =1;j<=t;j++)
    {
        sum =0 ;
        ans =0 ;
        cin>>s;

        cin>>smax;

        sum +=smax[0] - '0';
        for(int i=1 ;i<=s;i++)
        {
            //  cout<<sum<<" "<<ans<<endl;
            if(sum<i && (smax[i] -'0') >0)
            {
                ans += i- sum;
                sum = i ;
            }
            sum += smax[i] -'0';
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
    }
}


