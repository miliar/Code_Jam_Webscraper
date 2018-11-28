#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

char S[2000];

void read() {
	scanf("%ss", S);

}


char res[2000];
char t1[2000];
char t2[2000];

void process() {
	memset(res, 0, sizeof(res));
	for (int i = 0; S[i]; i++) {
		t1[0] = S[i];
		t2[i] = S[i];
		t1[i+1] = t2[i+1] = 0;
		for (int j = 0; j < i; j++) {
			t1[j+1] = res[j];
			t2[j] = res[j];
		}
		if (strcmp(t1, t2) > 0) {
			strcpy(res, t1);
		} else {
			strcpy(res, t2);
		}
	}
	printf("%s\n", res);
}

int main() {
	
	int cases;

	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);

		read();
		process();
	}

	return 0;
}
