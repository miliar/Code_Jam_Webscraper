#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:16777216")
#include <ctime>
#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 
#include <cstdarg>
using namespace std; 
typedef vector<int> vi; 
typedef vector<string> vs; 
typedef pair<int,int> pii; 
typedef long long ll; 
typedef istringstream iss;
#define FOR(i,f,n) for(int i=f; i<n; ++i) 
#define sz(a) ((int)a.size()) 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define pb push_back 
#define all(a) a.begin(),a.end()
#define mp make_pair 
#define inf 1000000000 
#define X first
#define Y second
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = b%a, b = t; return a+b; }
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if (p&1) r = r*a; a = a*a; p >>= 1; } return r; }
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - a/b*y1; return g; }
template<class T> inline T Floor(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return (a-b+1)/b; return a/b; }
template<class T> inline T Ceil(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return a/b; return (a+b-1)/b; }
void print(const char *fmt, ...)  { va_list args; va_start(args, fmt); vprintf(fmt, args); vfprintf(stderr, fmt, args); va_end(args); }

int refnum[111];
int refsize;
int size, ssize;
int num[111];
int numnum[111];
bool tooBig;

bool isPalindrome() 
{
	FOR(i,0,ssize+1)
		numnum[i] = 0;

	FOR(i,0,size)
		FOR(j,0,size)
			numnum[i+j] += num[i]*num[j];

	if (numnum[ssize-1] == 0)
		throw new exception("NO!!!");

	if (refsize < ssize)
		tooBig = true;
	else if (refsize > ssize)
		tooBig = false;
	else 
	{
		for (int i=0; i<ssize; ++i)
		{
			if (numnum[i] > refnum[i])
			{
				tooBig = true;
				break;
			}
			else if (numnum[i] < refnum[i])
			{
				break;
			}
		}
	}

	if (tooBig)
		return false;

	for (int i=0; i<ssize; ++i)
	{
		if (numnum[i] >= 10)
			return false;
	}
	return true;
}

int doit(int p, int pp, int sum) 
{
	if (tooBig)
		return 0;

	if (p > pp) 
		return isPalindrome() ? 1 : 0;

	int res = 0;
	FOR(i,(p==0?1:0),4) 
	{
		sum += p == pp ? i : i+i;
		if (sum < 10)
		{
			num[p] = num[pp] = i;
			res += doit(p+1, pp-1, sum);
		}
	}
	return res;
}

int count() 
{
	tooBig = false;
	int sum = 0;
	for (int i=1; i<=51; ++i)
	{
		size = i;
		ssize = size+size-1;
		sum += doit(0, i-1, 0);
	}
	return sum;
}

void inputNum()
{
	char buf[256];
	
	scanf("%s", buf);
	for (refsize=0; buf[refsize]; ++refsize) {
		refnum[refsize] = buf[refsize] - '0';
	}
}

void decrement() 
{
	// if ONE
	if (refsize==1 && refnum[0] == 0)
	{
		refnum[0] = 0;
		return;
	}

	refnum[refsize-1] -= 1;
	// DECREMENT
	for (int i=refsize-1; i>=0; --i)
	{
		if (refnum[i] >= 0)
			break;
		refnum[i] += 10;
		refnum[i-1] -= 1;
	}

	// IF SIZE DECREASED
	if (refnum[0] == 0) 
	{
		FOR(i,1,refsize)
			refnum[i-1] = refnum[i];
		refsize -= 1;
	}
}

int N, M, K;
int main()
{
	freopen("inB.txt", "r", stdin);
	freopen("outB.txt", "w", stdout);
	clock_t startTime = clock();

	int Cases;
	scanf("%d", &Cases);
	FOR(Case,0,Cases)
	{
		print("Case #%d: ", Case+1);

		inputNum();
		decrement();
		int a = count();

		inputNum();
		int b = count();

		print("%d\n", b-a);
	}

	clock_t endTime = clock();
	fprintf(stderr, "\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
	return 0;
} 
