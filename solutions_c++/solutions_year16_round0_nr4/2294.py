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

template<class T>
T gcd(T a,T b) { if(a < b)return gcd(b,a); if(b==0)return a; return gcd(b,a%b); }

const int maxn = 100000005;
//const int maxn = 1000005;
vector<bool> p(maxn,true);
vector<int> primes(0);

void init()
{
    p[0] = p[1] = false;
    int i,j;
    for(i = 2; i * i <= maxn; i++)if(p[i])
    {
        primes.push_back(i);
        for(j = i + i; j < maxn; j += i)p[j] = false;
    }
}

Long toa(int n,int b)
{
    Long res = 0,m = 1;
    while(n)
    {
        if(n & 1)res += m;
        m *= b;
        n >>= 1;
    }
    return res;
}

string getv(int n)
{
    string s = "";
    while(n){ if(n & 1)s += '1'; else s += '0'; n >>= 1; }
    reverse(li(s));
    return s;
}

bool isPrime(Long n, int &d)
{
    int i;
    foo(i,0,primes)
    {
        if(primes[i] > n)return true;
        if(0 == n%primes[i])
        {
            d = primes[i];
            return false;
        }
    }
    return true;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int Case,t,n,i,j,m; init();
	scanf("%d",&t);
	vector<Long> v(11);
	vector<int> divisor(11);
	fo(Case,1,t+1)
	{
		printf("Case #%d:\n",Case);
        cin >> n >> j; n--;
        n = (1 << n); n++;

        while(j)
        {
            for(i = 2; i < 11;i++)
            {
                v[i] = toa(n,i);
                if(isPrime(v[i],divisor[i]))break;
            }
            if(i == 11)
            {
                j--;
                cout << getv(n);
                for(i = 2; i < 11; i++)cout << " " << divisor[i];
                cout << endl;
            }
            n += 2;
        }
		//cout << endl;
	}
	return 0;
}

