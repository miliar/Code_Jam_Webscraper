#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	
	int T;
	scanf("%d", &T);
	
	for(int k = 1; k <= T; k++) {
		
		int N;
		scanf("%d", &N);
		
		vector<double> na;
		vector<double> ke;
		
		for(int i = 0; i < N; i++) {
			double a;
			scanf("%lf", &a);
			na.push_back(a);
		}
		
		for(int i = 0; i < N; i++) {
			double a;
			scanf("%lf", &a);
			ke.push_back(a);
		}
		
		sort(na.begin(), na.end());
		sort(ke.begin(), ke.end());
		
		int warp = 0;
		
		int ni = 0;
		int ki = 0;
		int nn = N;
		int kn = N;
		
		while(ni != nn) {
			if(na[nn-1] > ke[kn-1]) {
				ki++;
				nn--;
				warp++;
			} else {
				nn--;
				kn--;
			}
		}
		
		ni = 0;
		ki = 0;
		nn = N;
		kn = N;
		
		int dewarp = 0;
		
		while(ni != nn) {
			if(na[ni] > ke[ki]) {
				dewarp++;
				ni++;
				ki++;
			} else {
				kn--;
				ni++;
			}
		}
		
		printf("Case #%d: %d %d\n", k, dewarp, warp);
	}
	
	return 0;
}
