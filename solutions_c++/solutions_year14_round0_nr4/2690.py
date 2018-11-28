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

double aa[1100]; int aap;
double bb[1100]; int bbp;
bool asc(double a,double b) {
	return a<b;
}
bool dsc(double a,double b) {
	return a>b;
}
void solve() {
	int n; cin >> n;
	aap=bbp=n;
	for(int i=0;i<n;i++) cin >> aa[i];
	for(int i=0;i<n;i++) cin >> bb[i];
	sort(aa,aa+aap,asc);
	sort(bb,bb+bbp,asc);

	int ap=aap-1,bp=bbp-1;
	int ans=0;
	for(;ap>=0 && bp>=0;) {
		if(aa[ap]>bb[bp]) {
			ap--;bp--;ans++;
		} else bp--;
	}
	cout << ans << " ";

	ap=aap-1,bp=0; ans=0;
	sort(aa,aa+aap,dsc);
	for(;ap>=0 && bp<n;) {
		if(aa[ap]>bb[bp]) {
			bp++;
		} else {
			ap--;bp++;
		}
	}
	cout << ap+1 << endl;
	//for(int i=0;i<aap;i++) cout << aa[i] << TAB ; cout << endl;
}
int main(){
    freopen("D-large.in","r",stdin);
	freopen("out.out","w",stdout);


	int cas=0;
	int t; cin >> t;
	while(t--) {
		printf("Case #%d: ",++cas);
		solve();
	}
}