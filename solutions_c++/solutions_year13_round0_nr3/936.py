#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vI;
typedef vector<string> vS;
typedef pair<int, int> pI;
typedef map<int, int> mI;
typedef map<string, int> mSI;
typedef set<int> sI;
typedef set<pI> spI;
typedef priority_queue<int> qmax;
typedef priority_queue<int, vector<int>, greater<int> >qmin;
typedef map<int, int>::iterator mI_it;
typedef set<int>::iterator sI_it;

#define TWO(k)  (1<<(k))
#define LTWO(k) (((LL)(1)<<(k)))
#define MIN(a,b) ( (a)<(b)?(a):(b) )
#define MAX(a,b) ( (a)>(b)?(a):(b) )
#define LS(x) 	 ((x)<<1)
#define RS(x) 	 (((x)<<1)+1)
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define B begin()
#define E end()
#define F0(i, n) for( int (i) = 0; (i) < (n); (i)++)
#define F1(i, n) for( int (i) = 1; (i) <= (n); (i)++)
#define zero(i) memset((i),0,sizeof((i)))

const double PI = acos(-1.0);
const double EPS = 1e-9;
const int ioo = (~0)-(1<<31);
const LL loo = (~(LL)0)-((LL)1<<63);

bool flag[1005] = {0};
int sum[1005] = {0};

void build()
{
    flag[1]=flag[4]=flag[9]=flag[121]=flag[484]=1;
    F1(i,1000)
    {
        if( !flag[i]) sum[i] = sum[i-1];
        else sum[i] = sum[i-1] + 1;
    }
}

bool fands( LL x)
{
    string ans = "";
    while( x)
    {
        ans += (char)('0'+x%10);
        x/=10;
    }
    int l = ans.length();
    F0(i,l)
    {
        if( ans[i] != ans[l-1-i]) return 0;
    }
    return 1;
}

LL res[41]={0, 1L,
4L,
9L,
121L,
484L,
10201L,
12321L,
14641L,
40804L,
44944L,
1002001L,
1234321L,
4008004L,
100020001L,
102030201L,
104060401L,
121242121L,
123454321L,
125686521L,
400080004L,
404090404L,
10000200001L,
10221412201L,
12102420121L,
12345654321L,
40000800004L,
1000002000001L,
1002003002001L,
1004006004001L,
1020304030201L,
1022325232201L,
1024348434201L,
1210024200121L,
1212225222121L,
1214428244121L,
1232346432321L,
1234567654321L,
4000008000004L,
4004009004004L,
200000000000000L};

int num1( LL x)
{
    for( int i = 0; i <= 39;i++)
    {
        if( x >= res[i] && x < res[i+1]) return i;
    }
    return 0;
}

int main()
{
//    freopen("out.txt","w",stdout);
//    freopen("C-large-1.in","r",stdin);
    int t, test = 0;
    cin>>t;
    build();
    while(t--)
    {
        cout<<"Case #"<<++test<<": ";
        LL a,b; cin>>a>>b;
        cout<<num1(b)-num1(a-1)<<endl;
        
    }
//    for( LL i = 1; i <= 10000000; i++)
//    {
//        if( fands(i) && fands(i*i)) cout<<i*i<<endl;
//    }
    return(0);
}

