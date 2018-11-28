#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>

using namespace std;

int main() {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B.out","w",stdout);
    int t;
    cin >> t;
    int cas = 1;
    while(t --) {
	double c,f,x;
	cin >> c >> f >> x;
	double pre = x/2.0;
	double ans = 0;
	double ret = 0;
	for(int i = 0 ;  ; i++ ){
	    ans += c/(2.0+i*f);
	    ret = ans + x/(2+f*(i+1));
	    if(ret - pre > 1e-8) {
		ret = pre;
		break;
	    }
	    pre = ret;
	}
	printf("Case #%d: %.7f\n", cas ++, ret);
    }
    return 0;
}
