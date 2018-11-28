#include<stdio.h>
#include<map>
#include<set>
#include<vector>
#include<iostream>
#include<stdio.h>
#include<assert.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>
#include<math.h>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
#define For(i,s,e) for(i=s;i<e;i++)
#define ss(a) scanf("%s",a)
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define sf(a) scanf("%f",&a)
#define sd(a) scanf("%lf",&a)
#define ps(a) printf("%s\n",a)
#define pi(a) printf("%d\n",a)
#define pl(a) printf("%lld\n",a)
#define pd(a) printf("%lf\n",a)
#define LL long long
#define MOD 1000000

using namespace std;
 
double mysol() {
	double C, F, X, f = 2, tfarm = 0;
	scanf("%lf%lf%lf", &C, &F, &X);
	int farm = 1;
	double out = tfarm + X / f, newans;
	while(true) {
		tfarm += C / f;
		f += F;
		newans = tfarm + X / f;
		if(newans < out) {
			out = newans;
		} else {
			break;
		}
	}
	return out;
}
 
int main() {

	int t,i;
	si(t);
	for(i = 1; i <= t; i++) {
		printf("Case #%d: %.7lf\n", i, mysol());
	}
	return 0;
}

