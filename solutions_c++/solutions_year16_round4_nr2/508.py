#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
double a[1000];
int n,k;
double p[1000];
int r;

double s[1000][1000];
double temp[1000][1000];

double f() {
	for(int i=0;i<=k;i++) for(int j=0;j<=k;j++) {s[i][j] = 0.0;temp[i][j]=0.0;}
	s[0][0] = 1.0; 
	for(int i=0;i<k;i++) {
		for(int j=0;j<=i;j++) {
			if(j < k/2 && i-j <= k/2) {
				temp[j+1][i-j] += p[i] * s[j][i-j];
			}
			
			if(i-j < k/2 && j <= k/2) {
				temp[j][i-j+1] += (1-p[i]) * s[j][i-j];
			}
		}
		
		int zz = min(k/2, i+1);
		for(int j=0;j<=i+1;j++) {
			s[j][i+1-j] = temp[j][i+1-j];
		}
	}
	//for(int i=0;i<=k/2;i++) {for(int j=0;j<=k/2;j++) cout << s[i][j] << " "; cout << endl;}
	return s[k/2][k/2];
}

double compute(int ind) {
	r = 0;
	for(int i=0;i<ind;i++) p[r++] = a[i];
	for(int i=0;i<k-ind;i++) p[r++] = a[n-1-i];
	//for(int i=0;i<k;i++) cout << p[i] << " "; cout << endl;
	return f();
}
int main(int argc, char *argv[]) {
	freopen("A.in","r",stdin);
	freopen("A.txt","w",stdout);
	int t;
	double ans;
	cin >> t;
	for(int aa=0;aa<t;aa++) {
		cin >> n >> k;
		for(int i=0;i<n;i++) cin >> a[i];
		
		sort(a,a+n);
		ans = 0.0;
		for(int i=0;i<=k;i++) {
			ans = max(ans, compute(i));
		}
		
		cout << "Case #" << aa+1 << ": " << ans << endl;
		
	}
}