
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())

//double binp[2][50000]

double binom(int i, int j) {
	if(j==0) return 1;
	if(j<0) return 0;
	return binom(i-1,j-1)*i/j;
}

double doit(int sides, int m, int rem) {
	if(m==sides+1) return 0;
	//cout << sides << " " << m << " " << rem << endl;
	double ret1=0,ret2=0;
	for(int i=m; i<=min(rem,sides); i++) if(rem-i<=sides) ret1+=binom(rem,i);
	for(int i=0; i<=min(min(m-1,rem),sides); i++) if(rem-i<=sides) ret2+=binom(rem,i);
	//cout << ret1 << " " << ret2 << endl;
	return ret1/(ret1+ret2);
}

double doit2(int side1, int side2, int m, int rem) {
	if(m==0) return 1;
	if(rem==0) return 0;
	if(side1==0) return doit2(side1,side2-1,m-1,rem-1);
	if(side2==0) return 0;
	return (doit2(side1-1,side2,m,rem-1)+doit2(side1,side2-1,m-1,rem-1))/2;
}

int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		cout << "Case #" << ts << ": ";
		int N,X,Y;
		cin >> N >> X >> Y;
		//cout << N << " " << X << " " << Y << endl;
		if(X<0) X=-X;
		int cur=1, i;
		for(i=5; cur+i<=N; i+=4) cur+=i;
		//cout << cur << " " << N << " " << i << endl;
		i--;
		if((X+Y)/2<i/4) cout << "1.0" << endl;
		else if((X+Y)/2>i/4) cout << "0.0" << endl;
		else if(X==0) cout << "0.0" << endl;
		else {
			cout << doit2(i/2, i/2, i/2-X+1, N-cur) << endl;
			//cout << doit(i/2, Y+1, N-cur) << endl;
		}
        }
}
