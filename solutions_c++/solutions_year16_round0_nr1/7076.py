#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

bool numCheck[10];

void updateNumber(int num) {
	while (num > 0) {
		numCheck[num % 10] = true;
		num /= 10;
	}
}

bool isComplete() {
	for (int i = 0; i < 10; i++)
		if (!numCheck[i])
			return false;
	return true;
}

int main() {
	int t, n;
	FILE *fp = NULL;
	fp = fopen("A-large.in", "r");
	FILE *fp2 = NULL;
	fp2 = fopen("output.txt", "w");
	fscanf(fp, "%d", &t);

	for (int i = 1; i <= t; i++) {
		fscanf(fp, "%d", &n);
		memset(numCheck, false, sizeof(numCheck));

		if (n == 0) {
			fprintf(fp2, "Case #%d: INSOMNIA\n", i);
		}
		else {
			long long curr = (long long)n;
			bool complete = false;

			updateNumber(curr);
			complete = isComplete();
			
			while (!complete) {
				curr = curr + n;
				updateNumber(curr);
				complete = isComplete();
			}
			fprintf(fp2, "Case #%d: %lld\n", i, curr);
		}
	}

	return 0;
}