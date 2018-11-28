/*
ID: Tariqul
PROG: 
LANG: C++
*/

#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector>

using namespace std; 

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) fo(i,j,sz(v))
#define Foo(i,j,v) Fo(i,j,sz(v))
#define li(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define CLR(a,v) memset((a),(v),sizeof(a))
#define inf 1000000001
//typedef long long Long;
typedef __int64 Long;

#define eps 1e-9

#define two(X) (1<<(X))
#define twoL(X) (((Long)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)

char BUFFER[100000 + 5];
bool readn(int &n)	{ return scanf("%d",&n) == 1; } 
bool readl(Long &n)	{ return scanf("%I64d",&n) == 1; } 
bool readd(double &n){ return scanf("%lf",&n) == 1; } 
bool reads(string &s){ s = ""; int n = scanf("%s",BUFFER); if(n == 1)s = BUFFER; return n == 1; }
bool readln(string &s){ char *valid = gets(BUFFER); if(valid)s = BUFFER; return ((bool)valid); }

const int maxn = 105;
int A[maxn][maxn],N,M;

void input()
{
	cin >> N >> M;
	int i,j;
	fo(i,0,N)fo(j,0,M)cin >> A[i][j];
}

bool can(int pi,int pj)
{
	//if(pi == 0 || pj == 0 || pi == (N - 1) || pj == (M - 1) )return true;
	int i,j;

	j = pj; fo(i,0,N)if(i != pi)if(A[i][j] > A[pi][pj])break; if(i == N)return true;	

	i = pi; fo(j,0,M)if(j != pj)if(A[i][j] > A[pi][pj])break; if(j == M)return true;	

	return false;
}

bool possible()
{
	int i,j;
	fo(i,0,N)fo(j,0,M)if(false == can(i,j))return false;	
	return true;
}

int main()
{
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	int Case,t;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{		
		input();
		printf("Case #%d: ",Case);
		if(possible())cout << "YES";
		else cout << "NO";
		cout << endl;
	}
	return 0;
} 

