#include<string>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<cmath>
#include<algorithm>
#include<iomanip>

using namespace std;

#define maxn 1000+10
#define oo 1000000000

typedef long long LL;

double C, F, X;

void Input() {
	scanf("%lf%lf%lf",&C,&F,&X);
}

void Solve(int Test) {
	double res = 0.0, t = 2.0;
	while (X / t > C / t + X / (F + t)) {
		res += C / t;
		t += F;
	}
	res += X / t;
	printf("Case #%d: %.7lf\n",Test,res);
}

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i = 1; i <= t; i++) {
    	Input();
    	Solve(i);
	}
    return 0;
}

