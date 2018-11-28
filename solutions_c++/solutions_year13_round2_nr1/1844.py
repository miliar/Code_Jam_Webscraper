//cc:Kartik Singal@ka4tik
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cassert>
#include<vector>
#include<string>
#include<iomanip>
#include<cstring>
#include<sstream>
#include<bitset>
#include<cstdio>
#include<cmath>
#include<climits>
#include<ctime>
#include<string>
#include<fstream>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#ifndef ONLINE_JUDGE
#define DEBUG 1
#include<conio.h>
#endif

using namespace std;

#define LL                    long long
#define ss(n)                 scanf("%s",n)
#define P(x)                  printf("%d\n",x);
#define Pll(x)                printf("%lld\n",x);
#define rep(x,n)              forr(x,0,n)
#define all(c)                (c).begin(),(c).end()
#define pb                    push_back
#define MOD                   1000000007
#define ones5                 11111
#define ones6                 111111
#define ones7                 1111111
#define ones8                 11111111
#define X                     first
#define Y                     second
#define db(x) 		          if(debug) cout << #x << " : " << x <<endl;
#define db2(x,y) 	          if(debug) cout << #x << " : " << #y <<" : " << x <<" "<<y<<endl;
#define db3(x,y,z) 	          if(debug)	cout << #x << " : " << #y <<" : " << #z<<" : "<< x <<" "<<y<<" "<<z<<endl;
#define dbs(str)	          if(debug) puts("str");
#define forr(x, b, e)         for (int x = (b); x <= (e); x++)
#define foreach(it,container) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define iii                   pair<pair<int,int>,int>
#define ii                    pair<int,int>
#define vi                    vector<int>
#define bitcount(n)           __builtin_popcount(n)

const int debug=1;
template<typename T> T gcd(T a, T b) { return (b == 0) ? abs(a) : gcd(b, a % b); }
template<typename T> inline T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<typename T> inline T mod(T a, T b) { return (a % b + b) % b; }
template<typename T> inline string tostring(const T& x) { ostringstream  os; os << x; return os.str(); }
inline int toint(const string& s) { istringstream  is(s); int x; is >> x; return x; }
inline double todouble(const string& s) { istringstream  is(s); double x; is >> x; return x; }
inline string tobinary( int a) { string s; while( a != 0 ) { s = (char)(a%2+'0') + s; a>>=1; } return s; }
int dx[] = {0, 1, 0, -1};int dx2[] = {0, 1, 0, -1,1,-1,1,-1};
int dy[] = {1, 0, -1, 0};int dy2[] = {1, 0, -1, 0,1,-1,-1,1};
long long modexp(int n, int p) {long long r = 1, b = n;while(p > 0) {if(p & 1) { r = r * b; if(r >= MOD) r %= MOD; }p >>= 1;b = b * b; if(b >= MOD) b %= MOD;}return r;}
template<class T> inline void s( T &n ) {n=0;T ch=getchar();T sign=1;while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getchar();}while( ch >= '0' && ch <= '9' )n=(n<<3)+(n<<1)+ ch-'0', ch=getchar();n=n*sign;}

/*Main Code Begins Now*/

#define NAME "problem"

void gernatetests(int N)
{
  srand(time(NULL));
  ofstream myfile;
  myfile.open (NAME "in.txt");
  myfile<<N<<endl;
  for(int i=0;i<N;i++)
  myfile<<rand()<<" ";

  myfile.close();
}
#define MAXN ones7
int testnum;
vector<LL> v;

void preprocess(void)
{

}

int solve()
{
	LL A,N;
	s(A);s(N);

	v.resize(N);
	for(int i=0;i<N;i++)
	{
		s(v[i]);
	}
	
	
	/*if(testnum==14)
	{
		
		
		cout<<A<<" "<<N<<endl;
		for(int i=0;i<N;i++)
	{
		cout<<v[i]<<endl;
	}
		
	}*/
	if(A==1)
	{
	printf("Case #%d: ",testnum);
	Pll(N);
	return 0;
	}
	sort(all(v));
	
	LL c=0;
	LL ans=N;
	for(int i=0;i<N;i++)
	{
		if(A>v[i])
		{
			A+=v[i];
		}
		else
		{
			while(A<=v[i])
			{
				A+=(A-1);
				c++;
				//db(c);
				if(c>ans)
				goto end;
					
			}
			
			A+=v[i];
		}
		ans=min(ans,c+(N-(i+1)));
	}
	ans=min(ans,c);
	
	end:
		
	printf("Case #%d: ",testnum);
	assert(ans>=0&&ans<=N);
	Pll(ans);

}
int main()
{
    #ifndef ONLINE_JUDGE
      //gernatetests(1000);
      freopen(NAME "in.txt", "r", stdin);
      freopen(NAME "out.txt", "w", stdout);
    #endif

    double cl = clock();
    preprocess();


    int T = 1;
    s(T);
    for(testnum=1;testnum<=T;testnum++)
    {
        solve();
    }


    fprintf(stderr, "Total Time: %lf\n", (clock() - cl) / CLOCKS_PER_SEC);
    return 0;
}





























