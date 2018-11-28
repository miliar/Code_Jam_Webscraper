#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAX 1024
using namespace std;

int N;
int mush[MAX];

int arbit() {
	int res = 0;
	for(int i = 1; i < N; i++) {
		if(mush[i - 1] > mush[i]) {
			res += (mush[i - 1] - mush[i]);
		}
	}
	return res;
}

bool works(int rate) {
	for(int i = 1; i < N; i++) {
		if(rate < (mush[i - 1] - mush[i])) {
			return false;
		}
	}
	return true;
}

int solve(int rate) {
	int res = 0;
	//printf("Rate = %d\n", rate);
	for(int i = 0; i < N - 1; i++) {
		res += min(rate, mush[i]);
	}
	return res;
}

int fixed() {
	int low = 0, high = 10001;
	while(1) {
		if(high - low <= 1) {
			if(works(low)) {
				return solve(low);
			}
			return solve(high);
		}
		int mid = (low + high) / 2;
		if(works(mid)) {
			//printf("Works for %d\n", mid);
			high = mid;
		} else {
			//printf("Doesn't work for %d\n", mid);
			low = mid + 1;
		}
	}
	return -1;
}

int main(int argc, char const *argv[]) {

	int cases;

	scanf("%d", &cases);
	for(int i = 1; i <= cases; i++) {
		scanf("%d", &N);
		for(int i = 0; i < N; i++) {
			scanf("%d", &mush[i]);
		}
		printf("Case #%d: %d %d\n", i, arbit(), fixed());

	}
	return 0;
}