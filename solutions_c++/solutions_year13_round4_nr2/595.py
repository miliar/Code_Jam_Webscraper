#include <map>
#include <cmath>
#include <queue>
#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
const long long MOD = 1000002013;
unsigned long long n, p;

long long f1(){
	long long l = 1 , r = 1LL<<n;
	while (l < r){
		long long m = (l+r+1)/2;
		long long ans = 0, tmp = m-1;
		for (long long j = 1; j <= n; j++) {
			if (!tmp) ans *= 2;
			else ans *= 2, ans += 1, tmp -=1, tmp /= 2;
		}
		if (ans + 1 <= p) l = m; else r = m-1 ;
	}
	return l-1;
}

long long f2() {
	long long l = 1, r = 1LL<<n;
	while (l < r){
		long long m = (l+r+1)/2 ;
		long long ans  = 0, tmp = (1LL<<n)-m;
		for (long long j = 1; j <= n; j++) {
			if (!tmp) ans *= 2, ans += 1;
			else ans *= 2, tmp -= 1, tmp /= 2;
		}
		if (ans + 1 <= p) l = m; else r = m-1 ;
	}
	return l-1;
}

int main(){
    int CAS, cas, i, op, j, k;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &CAS);
    for (cas = 1; cas <= CAS; cas++){
        scanf("%lld%lld", &n, &p);
        cout << "Case #" << cas << ": " << f1() << " " << f2() << endl;
    }
}
