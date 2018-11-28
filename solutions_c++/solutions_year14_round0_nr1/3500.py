#include <stdio.h>
#include <cstdlib>
#include <iostream>

#define inp(x) scanf("%d",&x)

using namespace std;

const char silly[] = "Bad magician!";
const char cheating[] = "Volunteer cheated!";

int main() {
	int T;
	int r,x;
	int set[4];
	bool setRemaining[4];
	int ansCount;
	int ans;

	inp(T);

	for (int t = 1; t <= T; t++) {
		inp(r);
		for (int j = 1; j <= 4; j++) {
			for (int k = 1; k <= 4; k++) {
				inp(x);
				if (j == r) {
					set[k - 1] = x;
				}
			}
			setRemaining[j - 1] = false;
		}

		inp(r);
		for (int j = 1; j <= 4; j++) {
			for (int k = 1; k <= 4; k++) {
				inp(x);
				if (j == r) {
					for (int i = 1; i <= 4; i++) {
						if (x == set[i - 1]) {
							setRemaining[i - 1] = true;
						}
					}
				}
			}
		}

		ansCount = 0;
		for (int i = 1; i <= 4; i++) {
			if (setRemaining[i - 1]) {
				ansCount++;
			}
		}

		if (ansCount == 0) {
			printf("Case #%d: %s\n",t,cheating);
		} else if (ansCount > 1) {
			printf("Case #%d: %s\n",t,silly);
		} else {
			for (int i = 1; i <= 4; i++) {
				if (setRemaining[i - 1]) {
					ans = set[i - 1];
				}
			}
			printf("Case #%d: %d\n",t,ans);
		}
	}

	return 0;
}
