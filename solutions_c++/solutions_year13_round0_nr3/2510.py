#include <set>
#include <bitset>
#include <queue>
#include <deque>
#include <set>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>

#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

using namespace std;

// -------------------- Khai bao cac container --------------------
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef pair <int, int> ii;
typedef vector <ii> vii;
typedef vector <string> vs;

typedef long long LL; //NOTES:int64
typedef unsigned long long ULL; //NOTES:uint64
typedef unsigned uint;

const double pi = acos(-1.0); //NOTES:pi
const double eps = 1e-11; //NOTES:eps
const int MAXI = 0x7fffffff;
const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};
const char dz[] = "SENW";

// -------------------- Dinh nghia lai cac phep toan --------------------
#define rep(i,n)        for (int i=0;i<n;i++)
#define loop(i,a,b)     for (int i=(a),_b=(b); i<_b; i++)
#define rloop(i,b,a)    for (int i=(b)-1,_a=(a); i>=_a; i--)
#define Reset(a,b)      memset((a),(b),sizeof(a))

#define endline         putchar('\n')
#define space           putchar(' ')
#define EXIT(x)         {cout << x;return 0;}

#define fi              first
#define se              second
#define pb              push_back
#define all(x)          (x).begin(),(x).end()
#define mp(X,Y)         make_pair(X,Y)
#define foreach(i, c)   for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c, x)   ((c).find(x) != (c).end())
#define sz(a)           a.size()

#define two(x)          (1 << (x))
#define two64(x)        (((int64)(1)) << (x))
#define S(x)            scanf("%d",&x);
#define input freopen("input.txt","r",stdin);
#define output freopen("output.txt","w",stdout);
#define deb(i,a,n) for(i=0;i<n;i++){cout<<a[i]<<" ";}
#define db(x,y)          printf("%d %d\n",x,y);
#define debug(args...)	{dbg,args; cerr<<endl;}
#define dline			cerr<<endl	
#define INF				(int)1e9
#define LINF			(long long)1e18
#define EPS				1e-9
#define maX(a,b)		((a)>(b)?(a):(b))
#define miN(a,b)		((a)<(b)?(a):(b))
#define abS(x)			((x)<0?-(x):(x))
#define mod             1000000007

struct debugger
{
	template<typename T> debugger& operator , (const T& v)
	{	
		cerr<<v<<" ";	
		return *this;	
	}
} dbg;

void debugarr(long long int * arr,int n)
{
	cout<<"{";
	for(int i=0;i<n;i++)
		cout<<arr[i]<<",";
	cout<<"}"<<endl;
}

long long int a[110];
int b[20],size;
// bool b[10000010];
bool check(long long int sq)
{
	int k=0;
	while(sq>0)
	{
		b[k++]=sq%10;
		sq/=10;
	}
	
	for(int i=0,j=k-1;i<=j;i++,j--)
	{
		if(b[i]!=b[j])
			return false;
	}
	return true;

}
void preprocess()
{
	int j,k=0;
	long long int i,l;
	for(i=1;i<=10000001;i++)
	{
		l=i*i;
		if(check(i))
			if(check(i*i))
		{a[k++]=l;}
	}
size=k;


}
long long int d[100]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL,100000020000001LL};
int main()
{
	input;
	output;
	int i,j,k,l,t,s=0,num;

	long long int *st,*en,n,m;
	S(t);
	size=40;
	// preprocess();
	// debug(size);
	 //debugarr(a,size);
	for(num=0;num<t;num++)
	{

		scanf("%lld %lld",&n,&m);
		st=lower_bound(d,d+size,n);
		// cout<<*st<<" "<<n<<endl;
		// if(*st!=n)
			// st++;
		en=lower_bound(d,d+size,m);
		 if(*en!=m)
			en--;
		// cout<<*st<<" "<<*en<<endl;
		printf("Case #%d: %d\n",num+1,max(0,en-st+1));

	}
	return (0);
}