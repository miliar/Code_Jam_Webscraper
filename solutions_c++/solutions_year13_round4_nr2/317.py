#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

#define LL long long
const int N = int(1e6) + 9;

LL n, p;

LL aa(){
	LL l = 1 , r = 1 << n;
	while (l < r) {
		LL m = (l+r+1)>>1 , res = 0, b = (m-1) ;
		for (LL j = 1 ; j <= n ; j++){
			if (!b) res <<= 1;
			else {
                res *= 2, res += 1;
                --b, b/=2;
			}
		}
		if (res+1<=p) l = m;
		else r = m-1;
	}
	return l-1;
}
LL bb(){
	LL l = 1 , r = 1 << n;
	while (l < r) {
		LL m = (l+r+1)>>1, res = 0, b = (1 << n)-m;
		for (LL j = 1 ; j <= n ; j++){
			if (!b) res <<= 1, res +=1;
			else {
                res *= 2;
                b-=1, b/=2;
			}
		}
		if (res+1<=p) l = m;
		else r = m-1;
	}
	return l-1;
}

int main(){
    int ca = 0, T;
   // freopen("in.txt", "r", stdin);
   freopen("bs.in", "r", stdin);
    freopen("bout.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        cin >> n >> p;
        printf("Case #%d: ", ++ca);
        cout << aa() << " " << bb() <<endl;
    }
}

