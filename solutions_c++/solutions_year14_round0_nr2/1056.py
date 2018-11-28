#pragma comment(linker,"/STACK:300000000")
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <stack>

#define gcd(a,b) __gcd((a),(b))
#define sqr(a) ((a)*(a))
#define odd(a) ((a)&1)
#define foru(i,n) for (int i=0;i<(n);i++)
#define ford(i,n) for (int i=(n)-1;i>=0;i--)
#define forab(i,l,r) for (int i=(l);i<=(r);i++)
#define forabd(i,r,l) for (int i=(r);i>=(l);i--)
#define fillchar(a,b) memset((a),(b),sizeof((a)))
#define pb push_back
#define F first
#define S second
#define all(x) x.begin,x.end
#define pw2(x) (1ull<<(x))
#define mp make_pair
#define filename "in"

const long double eps=1e-10;
const long double pi=acos(-1.0);
const long long inf=1000*1000*1000*1000*1000*1000;
const long long base=1000*1000*1000+7;

using namespace std;

long double c,f,x;
int step;

bool ok(long double t){
	long double res = t + t;
	long double speed = 2.;
	int kol = 0;
	while (kol < step){
		kol++;
		if (t - c/speed > eps){
			long double tt = t - c/speed;
			long double sp = speed + f;
			if (tt * sp - res > eps){
				res = tt * sp;
				t = tt;
				speed = sp;
			}
		} else
			break;
	}
	return (res - x > eps);
}

long double get(string s){
	long double res = 0;
	long double st = 1. / 10.;
	bool fl = false;
	for (int i = 0; i < s.size(); i++){
		if (s[i] == '.'){
			fl = true;
		} else
		if (fl){
			res = res + st * (0. + (long double)(s[i] - '0'));
			st = st / 10.;
		} else
			res = res * 10 + (long double )((s[i] -'0'));
	}
	return res;
}

string s1,s2,s3;

void solve(){
	cin >> s1 >> s2 >> s3;
	c = get(s1);
	f = get(s2);
	x = get(s3);
	if (c + c + c + c + c < f)
		step = 200000;
	else
		step = 4000;
	long double l = 0; long double r = x / 2.;
//	cout << ok(0) << endl;
	for (int iter = 1; iter < 300; iter++){
		long double mid = (r + l) / 2.;
//		cout << mid <<  " ____ " << endl;
		if (ok(mid))
			r = mid;
		else l = mid;
	}
	printf("%.8f\n", (double)((l+r) / 2.));
}

int main(){
	freopen (filename".in","r",stdin);
	freopen ("2.out","w",stdout);
	cout.precision(100);
	int test;
	cin >> test;
	for (int tt = 1; tt <= test; tt++){
		cout << "Case #" << tt << ": "; solve();
	}
	return 0;
}
