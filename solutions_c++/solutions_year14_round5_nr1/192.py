#include <iostream>
#include <cstdio>
using namespace std;

long long cases;
long long devices, device[1000001];
long long p, q, r, s;
double ans;

void updateAns(long long total, long long left, long long middle, long long right) {
	double l = (double)left/(double)total;
	double m = (double)middle/(double)total;
	double r = (double)right/(double)total;
	double their = max(l, max(m, r));

	ans = max(1.0 - their, ans);
}

int main() {
	cin>>cases;
	for (long long c = 1; c <= cases; c++) {
		// sliding window.
		long long total = 0;
		ans = 0;
		cin>>devices>>p>>q>>r>>s;
		for (long long i = 0; i < devices; i++) {
			device[i+1] = ((i) * p + q) % (r) + s;
			//cout<<device[i+1]<<" ";
			total += device[i+1];
			device[i+1] += device[i];
		}
		//cout<<"\n";

		// nope binary search
		for (long long i = 0; i < devices; i++) {
			long long left = device[i-1+1] - device[0];
			long long remaining = total - left;
			long long high = devices-1, low = i+1;
			while (high > low) {
				long long mid = (high+low+1)/2;
				if (device[mid+1] - device[i] <= remaining/2) {
					low = mid;
				} else {
					high = mid-1;
				}
			}
			if (high-1 >= i) {
				updateAns(total, left, device[high] - device[i], device[devices] - device[high]);
			}
			updateAns(total, left, device[high+1] - device[i], device[devices] - device[high+1]);
			if (high != devices-1) {
				updateAns(total, left, device[high+2] - device[i], device[devices] - device[high+2]);
			}
		}
		printf ("Case #%lld: %.10f\n", c, ans);
	}

}