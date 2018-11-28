#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;

typedef long long LL;

bool loss(int N, LL P, LL r) {
    for (int i=N; i--; ) {
	if (P&(1LL<<i)) { // L
	    r = min((r-1)/2, (1LL<<i)-1);
	} else { // W
	    return false;
	}
	if (r==0) return true;
    }
    return true;
}
bool win(int N, LL P, LL k) {
    LL r=(1LL<<N)-k-1;
    for (int i=N; i--; ) {
	if (P&(1LL<<i)) { // L
	    if (r!=0) return true;
	} else { // W
	    if (r==0) return false;
	    r = min((r-1)/2, (1LL<<i)-1);
	}
    }
    return true;
}
int main() {
    int T;
    scanf("%d", &T);
    for (int tc=1; tc<=T; tc++) {
	int N; LL P;
	cin>>N>>P;

	P--;
	LL ans1, ans2;
	LL l=0, r=1LL<<N, m;
	for (;r-l>1;) {
	    m=(l+r)/2;
	    if (loss(N, P, m)) l=m;
	    else r=m;
	}
	ans1=l;

	l=0; r=1LL<<N;
	for (;r-l>1;) {
	    m=(l+r)/2;
	    if (win(N, P, m)) l=m;
	    else r=m;
	}
	ans2=l;
	printf("Case #%d: %lld %lld\n", tc, ans1, ans2);
    }
    
    return 0;
}
