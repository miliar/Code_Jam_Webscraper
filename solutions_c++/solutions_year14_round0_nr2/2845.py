#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int main()
{
	int T;
	double C,F,X,now,needbefore,needafter,need;
	cin >> T;
	for(int t=1;t<=T;++t) {
		cin >> C >> F >> X;
		now=2.0;
		need=0.0;
		if(C>X) {
			printf("Case #%d: %.7lf\n",t,X/now);
			continue;
		}
		do {
			needbefore=(X-C)/now;
			needafter=X/(now+F);
			need+=C/now;
			now+=F;
		} while(needbefore>=needafter);
		printf("Case #%d: %.7lf\n",t,need+needbefore);
	}
	return 0;
}
