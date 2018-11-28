#include <iostream>
#include "cstring"
#include "cstdio"
using namespace std;
#define read	 freopen("C:\\Users\\XPX\\Desktop\\B-large.in","r",stdin)
#define write	 freopen("C:\\Users\\XPX\\Desktop\\outl.txt","w",stdout)
double C;
double F;
double X;

int main() {
	int T, cas = 0;

	read;
	write;
	cin>>T;
	double ans;
	while (T--) {
		cin>>C>>F>>X;
                printf("Case #%d: ", ++cas);
		if(C >= X) {
			printf("%.7f\n",X / 2);
		}
		else {
			ans = 0;
			double v = 2;
			while(true) {
				ans += C / v;
				double t0 = (X - C) / v;
				double t = X / (v + F);
				if(t0 > t) {
					v += F;
				}
				else {
					ans += t0;
					break;
				}
			}
			printf("%.7f\n",  ans);
		}
	}
	return 0;
}
