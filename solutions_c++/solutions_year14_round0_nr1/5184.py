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
	FILE *fi = fopen("output1.txt","w");
	
	for(int t1 = 1; t1 <= t; t1++){
		int a[4][4], b[4][4];
		int n1, n2;
		cin >> n1;
		lopi(0, 4){
			lopj(0,4){
				cin >> a[i][j];
			}
		}
		cin >> n2;
		lopi(0, 4){
			lopj(0,4){
				cin >> b[i][j];
			}
		}
		int ans=0,aaa;
		lopi(0,4){
			lopj(0, 4){
				if(a[n1-1][i] == b[n2-1][j]) {aaa = a[n1-1][i];ans++;}					
			}			
		}
		if(ans == 0){
			fprintf(stdout, "Case #%d: Volunteer cheated!\n",t1);					
		}
		else if(ans == 1){
			fprintf(stdout, "Case #%d: %d\n",t1,aaa);					
		}
		else{
			fprintf(stdout, "Case #%d: Bad magician!\n",t1);					
		}
		
	}
	fclose(fi);	
  	return 0;
}
/*
1
6 6 10
1 1 1 8 7 7
*/