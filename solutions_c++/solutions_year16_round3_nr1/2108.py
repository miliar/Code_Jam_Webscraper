#include <stdio.h>
#include <vector>

using namespace std;

int T;
int N;


int arr[3000];


int hap;
int half;
int ho() {
	int max = 0;
	int maxidx =N;
	hap = 0;
	for (int i = 0; i < N; i++) {
		hap += arr[i];
		if (arr[i] > max) {
			max = arr[i];
			maxidx = i;
		}

	}
	half = hap / 2;
	return maxidx;
}
int main() {
	int a;
	scanf("%d", &T);

	for (int ii = 1; ii <= T; ii++) {
		scanf("%d", &N);

		for (int i = 0; i < N; i++) {
			scanf("%d", arr+i);
		}


		printf("Case #%d: ",ii);

		while (1) {
			int idx1, idx2, idx3;
			idx1 = ho();
			if (idx1 == N) {
				break;
			}
			arr[idx1]--;
			
			idx2 = ho();
			if (idx2 == N) {
				printf("%c", 'A' + idx1);
				break;
			}
			arr[idx2]--;
			idx3 = ho();
			if (idx3 == N) {

				printf("%c%c",'A'+idx1, 'A' + idx2);
				break;
			}

			if (arr[idx3] > half) {
			
				printf("%c ", 'A' + idx1);
				arr[idx2]++;
			}
			else {
				printf("%c%c ", 'A' + idx1, 'A' + idx2);
			}

		}


		printf("\n");


	}

}