#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <ctype.h>
#include <bitset>
#include <assert.h>
#include <string.h>
 
using namespace std;
 
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))
 
#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second
typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;
LL a, b;
string s;
void gen()
{
	a = 0; b = 0;
	int i = 0;
	for(i = 0;s[i]!='/';i++)
	{
		a = (a*10)+s[i]-'0';
	}
	i++;
	for(;i<s.length();i++)
	{
		b = (b*10)+s[i]-'0';
	}
}

bool isinval(double f)
{
	double d = 0.5;
	int cou = 0;
	while(f != 0.0)
	{
		if(d <= f)
			f -= d;
		if(f == 0)return false;
		d /= 2;
		cou++;
		if(cou >= 13)return true;
	}
	return true;
}
int main()
{
	LL ite;
	cin>>ite;
	for(LL it = 1; it <= ite; it++)
	{
		cin>>s;	
		gen();
		double frac = (double)a/(double)b;
		if(isinval(frac))
		{
			cout<<"Case #"<<it<<": "<<"impossible"<<endl;
			continue;
		}
		double chk = 1.0;
		LL ans = 0;
		while(chk > frac)
		{
			//cout<<"called "<<chk<<endl;
			ans++;
			chk /= 2;
		}
		cout<<"Case #"<<it<<": "<<ans<<endl;
	}	
	return 0;
}
