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
#define pi (2*acos(0))
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

const int maxn = 10000000 + 100;

int digits[20];

bool isPalinddrome(Long n)
{	
	int i = 0,j = 0;
	while(n > 0){ digits[j++] = n%10; n /= 10; }
	
	for(j-- ; i < j; i++, j--)if(digits[i] != digits[j])return false;
	return true;
}

/*bool isPalinddrome(Long n)
{
	vector<int> digits(0);
	int i = 0,j = 0;
	while(n > 0){ digits.push_back(n%10); n /= 10; }
	j = sz(digits);	
	for(j-- ; i < j; i++, j--)if(digits[i] != digits[j])return false;
	return true;
}
*/

vector<Long> v;

void init()
{
	Long i; v.clear();
	fo(i,1,maxn)if(isPalinddrome(i))if(isPalinddrome(i*i))
	{		
		v.push_back(i*i);
	}
}

int main()
{		
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	init();	
	int Case,t; Long A,B; int cnt,i;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{		
		printf("Case #%d: ",Case);
		readl(A); readl(B);  cnt = 0;
		foo(i,0,v)cnt += (A <= v[i] && v[i] <= B);
		cout << cnt << endl;
	}
	return 0;
} 

