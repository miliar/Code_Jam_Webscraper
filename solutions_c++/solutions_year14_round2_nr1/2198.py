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
int calc(string S[], int n){
	int m[2][100];
	int i = 0, c = 0, j = 0;
	M(m,0);
	while(1){
		if(S[0][i] == S[1][j]){
			if(S[0][i] == '\0') break;
			int k1 = i, k2 = j;
			i++;
			while(S[0][i-1] == S[0][i]){
				i++;	
			}
			m[0][c] = i-k1;
			j++;
			while(S[1][j-1] == S[1][j]){
				j++;	
			}
			m[1][c] = j-k2;				
		}
		else
			return -1;
		c++;		
//		F(l,0,4) cout<< m[0][l] << " ";nl;	
//		F(l,0,4) cout<< m[1][l] << " ";nl;	
//		getchar();
	}
	int u = 0;
	int ass = 0;
	while(1){
		if(m[0][u] == 0 || m[1][u] == 0){
			break;
		}
		ass += 	abs(m[0][u] - m[1][u]);
		u++;
	}
//	cout << "out";
	return ass;
}
int main(){ 
    ios_base::sync_with_stdio(0);
	lli t,n;
    freopen("inp0.txt", "r", stdin);
    freopen("out0.txt", "w", stdout);
	cin >> t;
	for(int t1= 1; t1 <= t; t1++){
		cin >> n;
		string S[n];
		for(int i = 0; i < n; i++){
			cin >> S[i];
		}
		lli ans;
		ans = calc(S, n);
		fprintf(stdout, "Case #%d: ",t1);					
		if(ans == -1)
			fprintf(stdout, "Fegla Won\n");							
		else
		fprintf(stdout, "%d\n",ans);							
	}
  	return 0;
}
