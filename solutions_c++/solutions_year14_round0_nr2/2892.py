#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <string.h>
#include <queue>
#include <iomanip>
#include <map>
#include <string>
#include <time.h>
#include <stack>

using namespace std;
#define LL long long
#define MAXN 110
#define MAXE 55000
#define MOD 1000000007
#define ENTER putchar('\n');
#define TAB "\t"
#define PRINT(x) cout<<(x);
#define MAX(x,y) ((x)>(y)?(x):(y))
#define MIN(x,y) ((x)<(y)?(x):(y))
#define ABS(x) ((x)>0?(x):-(x))
#define EPS 1E-9
#define INF 0x3f3f3f3f
#define DEBUG for(int i=1;i<=20;i++){for(int j=1;j<=20;j++) {	cout << mp[i][j] << " ";	}	cout << endl;}
#define DEB(value) for(int i=1;i<=n;i++){PRINT(value[i]);TAB;}ENTER;
#define EINF 1E10
#define PI 3.1415926535
#define ULL unsigned long long

int dcmp(double x) {
	if(fabs(x) < EPS) return 0;
	else return x<0?(-1):1;
}
void solve() {
	double c,f,x;
	cin >> c >> f >> x;
	double ans=0.0;
	double speed=2.0;
	while(1) {
		double a=x/speed;
		double b=c/speed+x/(speed+f);
		//cout << a << TAB << b << TAB << ans << endl;
		if(dcmp(a-b)>0) {
			ans+=c/speed;
			speed+=f;
		} else {
			ans+=x/speed;
			break;
		}
	}
	cout << fixed << setprecision(7) << ans << endl;
}
int main(){
    freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);


	int cas=0;
	int t; cin >> t;
	while(t--) {
		printf("Case #%d: ",++cas);
		solve();
	}
}