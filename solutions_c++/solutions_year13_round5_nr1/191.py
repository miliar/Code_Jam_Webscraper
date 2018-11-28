#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;

typedef long long LL;

int T;
int N;
LL B;
LL X[40], Y[40];

double calc() {
    LL mi=Y[0]+X[0];
    double tmp=0, cnt=0;
    for (int j=0; j<37; j++) mi=min(mi, Y[j]+X[j]);

    for (int j=0; j<37; j++) {
	if (mi==Y[j]+X[j]) {
	    cnt += 1.0;
	    tmp += Y[j];
	}
    }
    return tmp*36/cnt;
}

double get(LL h, int k) {
    double ans=0;
    memset(Y, 0, sizeof Y);
    LL cst=0;

    for (int j=0; j<k; j++) {
	if (X[j]<=h) {
	    Y[j] = h-X[j];
	    cst += Y[j];
	} else {
	    return 0;
	}
    }
    for (int j=k; j<37; j++) {
	if (X[j]<=h) {
	    Y[j] = h-X[j] + 1;
	    cst+=Y[j];
	}
    }
    if (cst<=B) ans = max(ans, calc()-cst);

    return ans;
}

int main() {
    
    scanf("%d", &T);

    for (int tc=1; tc<=T; tc++) {
	cin>>B;
	scanf("%d", &N);
	memset(X, 0, sizeof X);
	for (int i=0; i<N; i++) cin>>X[i];
	sort(X, X+37);
	
	double ans=0;
	for (int i=1; i<37; i++) {
	    for (int j=1; j<=X[36]+B; j++) ans = max(ans, get(j, i));
	}
	printf("Case #%d: %.20f\n", tc, ans);
    }
    return 0;
}
