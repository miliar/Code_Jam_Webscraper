#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>

char input[101];
int arr[101];

void reverse(int index);
int find(int index);

int main() {
	int ts, ans, len;
	FILE *wfp;

	wfp = fopen("output.txt", "w");

#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#endif

	scanf("%d", &ts);

	for (int t = 1; t <= ts; t++) {
		ans = 0;

		scanf("%s", input);
		len = strlen(input);

		for (int i = 0; i < len; i++)
			if (input[i] == '-')
				arr[i] = 0;
			else
				arr[i] = 1;

		for (int i = len - 1; i >= 0; i--) {
			if(arr[i] == 0) {
				if (arr[0] == 0) {
					reverse(i);
					ans++;
				}
				else {
					int index = find(i - 1);
					reverse(index);
					ans++;
					reverse(i);
					ans++;
				}
			}
		}

		fprintf(wfp, "Case #%d: %lld\n", t, ans);
	}

	fclose(wfp);

	return 0;
}

void reverse(int index) {
	int tmp[101];

	for (int i = index; i >= 0; i--) {
		if (arr[i] == 0) {
			tmp[index - i] = 1;
		}
		else {
			tmp[index - i] = 0;
		}
	}

	for (int i = 0; i <= index; i++)
		arr[i] = tmp[i];
}

int find(int index) {
	int i;

	for (i = 1; i <= index; i++) {
		if (arr[i] != 1) {
			break;
		}
	}

	return i - 1;
}