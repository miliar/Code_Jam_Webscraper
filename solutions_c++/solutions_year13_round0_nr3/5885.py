#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <iostream>
#include<list>
#include<deque>
#include<iterator>
#include<sstream>

using namespace std;

#define FOR(i, a, b) for (int i(a) ; i < b; ++i)
#define FORD(i, a, b) for (int i(a) ; i > b; --i)
#define FORE(i, a, b) for (int i(a) ; i <= b; ++i)
#define FORDE(i, a, b) for (int i(a) ; i >= b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)

#define M(a) memset(&a,0,sizeof(a));
#define RES(i) cout<<"Case #"<<i<<": "<<
#define I cin>>
#define O cout<<
#define NL <<endl

#define ALL(c) (c).begin(), (c).end()

//typedef long long int64;
//typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

typedef vector<int> vi;
typedef vector<string> vs;

typedef map<int,int> mi;
typedef map<string,string> ms;

typedef set<int> si;
#include<stack>
#include<queue>
int maximum(int a,int b,int c)
{
	if (a>b)
		if (a>c)
			return a;
		else 
			return c;
	else if (b>c)
		return b;
	else return c;
}
//int arr[1001][1001];
bool b[1001];
char arr[4][4];
int eval(int a,int b, int x)
{
	if (arr[a][b] == x)
		return 1;
	return 0;
}
int getresult(int a, int b,int t)
{
	if ((t && a ==3) || a == 4) 
		return 1;
	if ((t && b ==3) || b == 4) 
		return 2;
	return 0;
}
int p1()
{
	int tc;
	cin>>tc;
	FOR(c,0,tc)
	{
		int e=0;
		FOR(i,0,4)
			FOR(j,0,4)
			{
				char c;
				cin>>c;
				arr[i][j]=c;
				e|=eval(i,j,'.');
			}
		int t,a,b;
		int t1,a1,b1;
		int result=0;
		FOR(i,0,4)
		{
			a=b=t=0;
			FOR(j,0,4)
			{
				a+=eval(i,j,'X');
				b+=eval(i,j,'O');
				t|=eval(i,j,'T');
			}
			result=getresult(a,b,t);
			if (result)
				break;
		}
		if (!result)
		{
			FOR(i,0,4)
			{
				a=b=t=0;
				FOR(j,0,4)
				{
					a+=eval(j,i,'X');
					b+=eval(j,i,'O');
					t|=eval(j,i,'T');
				}
				result=getresult(a,b,t);
				if (result)
					break;
			}
		}
		if (!result)
		{
			a=b=t=0;
			a1=b1=t1=0;
			for(int i=0,j=0;i<4;i++,j++)
			{
				a+=eval(i,j,'X');
				b+=eval(i,j,'O');
				t|=eval(i,j,'T');
				a1+=eval(i,3-j,'X');
				b1+=eval(i,3-j,'O');
				t1|=eval(i,3-j,'T');
			}
			int r1=getresult(a,b,t);
			int r2=getresult(a1,b1,t1);
			if (r1)
				result = r1;
			if (r2)
				result = r2;
		}
		if (result == 0)
		{
			if (e == 1)
				cout<<"Case #"<<c+1<<": "<<"Game has not completed"<<endl;
			else
				cout<<"Case #"<<c+1<<": "<<"Draw"<<endl;
		}
		else if (result==1)
			cout<<"Case #"<<c+1<<": "<<"X won"<<endl;
		else if (result==2)
			cout<<"Case #"<<c+1<<": "<<"O won"<<endl;
		
	}
	return 0;
}

bool ispalin(unsigned __int64 n)
{
	char buf[10000]={0};
	itoa(n,buf,10);
	char *a=buf;
	char *b=buf + (strlen(buf)-1);
	for(;a<b;a++,b--)
		if (*a!=*b)
			return false;
	return true;
}
int PerfectSquare(int n)
{
    int h = n & 0xF; // last hexidecimal "digit"
    if (h > 9)
        return 0; // return immediately in 6 cases out of 16.

    // Take advantage of Boolean short-circuit evaluation
    if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 )
    {
        // take square root if you must
        int t = (int) floor( sqrt((double) n) + 0.5 );
            return t*t == n;
    }
    return 0;
}
void p3()
{
	int tc;
	cin>>tc;
	FOR(c,0,tc)
	{
		unsigned __int64  a,b;
		cin>>a>>b;
		unsigned __int64 tot=0; 
		unsigned __int64 i=0;
		for(i=a; i<=b; i++)
		{
			if (ispalin(i) && PerfectSquare(i))
			{
				unsigned __int64  t=sqrt((double)i);
				if (ispalin(t))
						tot++;
			}
			
				
		}
		cout<<"Case #"<<c+1<<": "<<tot<<endl;
	}
}
int main(int argc, char* argv[])
{
	//p1();
	p3();
	return 0;
}

