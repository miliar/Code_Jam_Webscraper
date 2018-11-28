#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cmath>
#include<stack>
#include<fstream>
#include<sstream>
#include<map>
#include<algorithm>
#include<cassert>
#include<vector>
#include<climits>

#define DEBUG 0
#define SMALL 1
#define LARGE 0

using namespace std;
#if DEBUG
#define TRACE(a) cerr << "value of " << #a << ":" << a << endl
#define TRACE(a,b) TRACE(a);TRACE(b)
#define TRACE(a,b,c) TRACE(a,b);TRACE(c)
#define TRACE(a,b,c,d) TRACE(a,b);TRACE(c,d)
#else
#define TRACE(a) 
#define TRACE(a,b) 
#define TRACE(a,b,c) 
#define TRACE(a,b,c,d) 
#endif

#define si(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a);

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()


typedef long long int64;
typedef unsigned long long uint64;


#define MAX 1010
int arr[MAX];

int mul[4][4] = {{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
int fun(int a,int b) {
	bool sign=true; // +
	if(a<0) {sign  = !sign;
		a = -a;
	}
	if(b<0){ sign =! sign;
		b = -b;
	}
	int ans = mul[a-1][b-1];
	if(!sign) ans = -ans;
	return ans;

}
int main() {
#if SMALL
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small.out","w",stdout);
#endif
#if LARGE
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
#endif
	int T,D,N,K;
	string str="",str1;
	si(T);
	
	FOR(test,1,T) {
		si(N); si(K);
		char ch;
		scanf("%c",&ch);
		cin >> str;
		//REP(i,K) str = str+str1;
		bool is_i=false,is_j=false,is_k=false,is_complete=false;
		int l=str.length();
		int last = 1;
		REP(j,K) {
			REP(i,N) {
				last = fun(last,(str[i]-'i'+2));
				if(!is_i && last==2) {
					is_i = true;
					last = 1;
				}
				else if(is_i && !is_j && last==3) {
					is_j = true;
					last = 1;
				}
				else if(is_i && is_j && !is_k && last==4) {
					is_k = true;
					last = 1;
				}
			
			}
		}
		if(is_i && is_j && is_k && last == 1) {
			cout << "Case #"<< test << ": YES\n" ;
		}
		else {
			cout << "Case #"<< test << ": NO\n" ;
		}
	}
	return 0;
}
