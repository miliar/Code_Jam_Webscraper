#include <vector>
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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <ctime>

using namespace std;

typedef long long int lli;
typedef unsigned long long int llu;
typedef long double ld;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define sz sizeof
#define M(arr, x) memset(arr, x, sizeof(arr))
const int maxsize=(1<<20);
const int MOD=1000000007;
inline void ADDTO(int &a,int b) { a+=b; if (a>=MOD) a-=MOD; }
#define MUL(a,b) ((int)(((int64)(a))*((int64)(b))%MOD))
#define MAX 1000009
#define nl cout<<endl
#define spc cout<<" "
#define Sd(d) scanf("%d", &d)
#define Sl(d) scanf("%ld", &d)
#define Sll(d) scanf("%lld", &d)

#define F(i,s,e) for(lli i = s; i < e; i++)
#define D(i,s,e) for(lli i = s; i >= e; i--)

#define lopi(m,n) for(lli i = m; i < n; i++)
#define lopj(m,n) for(lli j = m; j < n; j++)
#define lopk(m,n) for(lli k = m; k < n; k++)
#define lop(m,n) for(lli i = m; i >= 0; i--)
int main(){ 
   ios_base::sync_with_stdio(0);
	lli t;
	cin >> t;
	FILE *fi = fopen("output2.txt","w");
	
	for(int t1 = 1; t1 <= t; t1++){
		double ans = 0.0, prev=0.0;
		double sum = 0.0, tmp;
		double c,f,x,r=2.0;
		cin >> c >> f >> x;
		ans = x/r;
		while(1){
			tmp = prev+(c/(r)) + (x/(r+f));
//			cout << "tmp = " << tmp << ": ans =" << ans << endl;
			if(tmp <= ans) {
				ans = tmp;
				prev += (c/r);
				r = r+f;
			}
			else break;
		}				
		fprintf(stdout, "Case #%d: %.7lf\n",t1,ans);					
	}
	fclose(fi);	
  	return 0;
}
