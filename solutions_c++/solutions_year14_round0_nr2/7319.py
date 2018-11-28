#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
	freopen("in.in","r",stdin);
    freopen("out","w",stdout);
	int T;
	double c, f, x;
	double ans, time_farm, rate;
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> c >> f >> x;
		ans = x/2; // no farm so far
		time_farm = 0;
		rate = 2;
		while(1) {
			// the time for building farm
			time_farm += c / rate;
			//printf("time farm: %f, ans: %f\n", time_farm, ans);
			if (time_farm + x/(rate+f) < ans) {
				// building new farm is better
				rate += f;
				ans = time_farm + x/rate;
				//printf("build a new farm\n");
			}else {
				// no more farm
				break;
			}
		}
		printf("Case #%d: %f\n", t, ans);
	}
	return 0;
}