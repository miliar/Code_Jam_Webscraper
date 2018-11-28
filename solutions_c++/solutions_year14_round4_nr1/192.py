//label : work
//By myf
//#pragma comment(linker, "/STACK:16777216")  //C++
#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#include <bitset>
#include <stack>
#include <complex>
#include <list>
#include <iomanip>

#define rep(i, n) for(int i = 0; i < (n); i++)
#define REP(i, l, r) for(int i = (l) ; i < (r); i++)
#define MP make_pair
#define PB push_back
#define Cls(x) memset(x,0,sizeof x)
#define Print(n,x) for(int i=0;i<(n);i++) cout<<x<<" ";cout<<endl;
#define foreach(i,n) for(__typeof(n.begin()) i=n.begin();i!=n.end();i++) //G++
#define F first
#define S second
#define X real()
#define Y imag()
#define Sqr(x) (x)*(x)
#define sign(x) ((x < -EPS) ? -1 : x > EPS)

using namespace std;

typedef long long LL;
typedef complex<double> Point;
typedef Point Vec;
typedef pair<Point, Point> Line;
typedef pair<int, int> pii;
//typedef complex<double> Comp;

const int M = 701;
const int MD = 1000000007;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);
const double EPS = 1E-6;

int n, cap;
int cnt[M];

int main(){
	int T;
	scanf("%d", &T);
	rep(cas, T){
		scanf("%d%d", &n, &cap);
		rep(i, M){
			cnt[i] = 0;
		}
		rep(i, n){
			int x;
			scanf("%d", &x);
			cnt[x]++;
		}
		int ans = 0;
		for(int i = cap; i >= 1; i--){
			for(int j = 1; j + j <= i; j++){
				if (j + j == i){
					while(cnt[j] >= 2){
						ans++;
						cnt[j] -= 2;
					}
				}
				else{
					while(cnt[j] >= 1 && cnt[i - j] >= 1){
						ans++;
						cnt[j]--;
						cnt[i - j]--;
					}
				}
			}
			while(cnt[i] >= 1){
				cnt[i]--;
				ans++;
			}
		}
		printf("Case #%d: %d\n", cas + 1, ans);
	}
	return 0;
}
