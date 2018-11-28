/* Cookie Clicker Alpha */
/* produced by wegnahz */
#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
using namespace std;
#define skip(x) for(int i=1;i<=(x);++i) getchar();
#define xx first
#define yy second
#define MP make_pair
#define two(X) (1<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define fill0(a) memset(a,0,sizeof(a));
typedef pair<int,int> ipair;
const int inf=0x3FFFFFFF;
const double pi=acos(-1.0);
const double eps=1e-8;
const int move[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
inline void show(int *a,int n){
  for (int i=0;i<=n;i++) cout<<a[i]<<' ';cout<<endl;}
int num,n,m;
int main(){
    int tt,ii;
    #ifndef ONLINE_JUDGE
    freopen("Cookie Clicker Alpha.in","r",stdin);
    freopen("Cookie Clicker Alpha.out","w",stdout);
    #endif
    cin >> tt;
    for (int ii = 1; ii <= tt; ++ii) {
    	double c, f, x;
    	cin >> c >> f >> x;
    	int nf = 0;
    	double ans = x / 2, base = 0;
    	while (1) {
    		++nf;
    		base += c / (2+(nf-1)*f);
    		double cur = base + x / (2+nf*f);
    		//cout << ans << ' ' << cur << endl;
    		if (cur < ans + 1e-8)
    			ans = cur;
    		else
    			break;
    	}
    	printf("Case #%d: %.7f\n", ii, ans);
    }
    return 0;
}
