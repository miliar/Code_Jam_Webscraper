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
		int n;
		cin >> n;
		bool check[n];
		M(check, 0);
		double a[n], b[n];
		lopi(0, n){
			cin >> a[i];
		}lopi(0, n){
			cin >> b[i];
		}
		sort(a, a+n);
		sort(b, b+n);
/*		lopi(0, n){
			cout << a[i] << ":" << b[i]<<endl;
		}
*/		/// Fair playing
//		lopj(0,n)cout << check[j] << " ";nl;
		int pts = 0;
		lopi(0, n){
			int f = 1;
			lopj(0, n){
				if(b[j] > a[i] && check[j] == 0){
					pts++;
					check[j] = 1;
					f = 0;
					break;
				}
			}
			if(f) lopj(0, n){if(check[j] == 0) {check[j]=1; break;}}
//			lopj(0,n)cout << check[j] << " ";nl;
		}
		int ans1 = n-pts;
		int ans2 = 0,c1=0, n1 = n-1, n2 = n-1,c2=0;
		lopi(0,n){
			if(a[c1] < b[c2]){
				c1++;
				n2--;
				continue;
			}
			else{
				ans2++;
				c1++;
				c2++;
			}		
		}
		fprintf(stdout, "Case #%d: %d %d\n",t1, ans2, ans1);
	}
	fclose(fi);	
  	return 0;
}
/*
		for(i = 0; i < n; i++){
			if(a[i] > b[n-1-i]) break;
		}
		cout << "i=" << i << endl;
		int ans2 = n-i;
		cout << "Non-Fair play = " << ans2 << endl;

*/