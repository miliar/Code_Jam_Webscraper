//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
#include<sstream>
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include <time.h>
#include<cmath>
#include<memory>
#include<memory.h>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef unsigned long long      ULL;
typedef long long               LL;

#define PB                      push_back
#define MP                      make_pair
#define X                       first
#define Y                       second
#define FOR(i, a, b)            for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b)           for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b)             memset(a, b, sizeof(a))
#define SZ(a)                   int((a).size())
#define ALL(a)                  (a).begin(), (a).end()
#define RALL(a)                 (a).rbegin(), (a).rend()
#define INF                     (1000000000)
#define FILL                    CLEAR

const int MOD = 1000002013;

void submit(){
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
}

LL f(LL n , LL p){
	if (p + 1 == (1LL << n)){
		return p;
	}
	LL t = 0;
		LL res = 0;
		while (res <= p){
			++t;
			res += 1LL << (n - t);
		}
	return (1LL << (t)) - 2;
}

int main()
{
	submit();

	int t;
	cin >> t;
	FOR(test,0,t){
		cerr << test << endl;
		cout << "Case #" << test + 1 << ": ";
		int n ; 
		LL p;
		cin >> n >> p;
		--p;
		cout << f(n , p) << ' ';
		++p;
		p = (1LL << n) - p;
		--p;
		cout << (1LL << n ) - f(n , p) -2  << endl;
	}

    return 0;
};