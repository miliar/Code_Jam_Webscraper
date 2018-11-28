#include <cstdio>
#include <set>
#include <algorithm>
#include <iterator>

int main() {
	using namespace std;
	int T;
	double C, F, X;
		
	scanf("%d", &T);
	for (int i=0; i<T; ++i) {
		scanf("%lf %lf %lf", &C, &F, &X);

		double t0 = 0;
		double fps = 2;
		
		while((C/fps + X/(fps+F)) < (X/fps)) {
			t0  += C/fps;
			fps += F;
		}
		
		t0+=X/fps;
		printf("Case #%d: %.7lf\n", i+1, t0);
	}
}