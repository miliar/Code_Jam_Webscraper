// Template v2
#define pb push_back
#define mp make_pair
#define det(a,b,c,d)  (a*d-b*c)
#define first x
#define second y
#define lsb(x) x & -x
#define l(x) (x<<1)
#define r(x) ((x<<1)|1)
#define PI   3.14159265358979323846
#include<fstream>
#include<vector>
#include<iomanip>
#include<map>
#include<set>
#include<algorithm>
#include<string.h>
#include<stack>
#include<unordered_map>
#include <bitset>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef pair<double, double> PKK;
// primes less than 100
const int PRIM[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}; const int CMAX = 100069;
const int MOD = 1000000007;
const int POW1 = 31;
const int MOD2 = 10429;
const int POW2 = 13;
const int P = 73;
const int NMAX = 105069;
const double EPS = 1e-7;
const int INF16 = 320000;
const int INF = 0x3F3F3F3F;
const LL INF64 = LL(1e18);
const int dx[]={-1,1,0,0};
const int dy[]={0,0,1,-1};

ifstream cin("trimitere.in");
ofstream cout("trimitere.out");
 
struct comb{
	int a, b, c;
	string s;
	comb(int a, int b, int c, string s)
	{
		this->a=a;
		this->b=b;
		this->c=c;
		this->s=s;
	}
	comb(){}
};

comb combine(comb l, comb r)
{
	comb n;
	n.a=l.a+r.a;
	n.b=l.b+r.b;
	n.c=l.c+r.c;
	n.s=l.s+r.s;
	return n;
}

comb A[15][200000];
int z[15];
int t,n,a,b,c;
void read()
{
	A[1][++z[1]]=comb(0,1,0,"P");
	A[1][++z[1]]=comb(1,0,0,"R");
	A[1][++z[1]]=comb(0,0,1,"S");
	for(int k=1; k<=13; ++k)
		for(int i=1; i<=z[k]; ++i)
			for(int j=i+1; j<=z[k]; ++j)
				A[k+1][++z[k+1]]=combine(A[k][i], A[k][j]);
	cin>>t;
	for(int tt=1; tt<=t; ++tt)
	{
		cout<<"Case #"<<tt<<": ";
		cin>>n>>a>>b>>c;
		n++;
		bool q=0;
		for(int i=1; i<=z[n] && !q; ++i)
		{
			if(A[n][i].a==a && A[n][i].b==b && A[n][i].c==c)
			{
				cout<<A[n][i].s<<"\n";
				q=1;
			}
		}
		if(!q)
			cout<<"IMPOSSIBLE\n";
	}
}
 
int main()
{
	cout<<setprecision(6)<<fixed;
    read();
    return 0;
}	