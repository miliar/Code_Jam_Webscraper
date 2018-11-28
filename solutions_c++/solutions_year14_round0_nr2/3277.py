#include<bits/stdc++.h>
using namespace std;

int main() {
	freopen("inn", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t,temp = 1;
	cin>>t;
	double c,f,x, times,time2,time1,rate;
	while(t--) {
		cin>>c>>f>>x;
		times = 0.0;
		rate = 2;
		while(1) {
			time1 = times + (x/rate);
			time2 = times + (c/rate) + (x/(rate + f));
			times += c/rate;
			rate += f;
			if(time1 < time2) {
				break;
			}
		}
		printf("Case #%d: %0.7lf\n",temp,time1);
		temp++;
	}
	return 0;
}
