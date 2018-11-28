#include <iostream>

bool ch_num(bool *arr) {
	for (int i = 0; i < 10; i++)
		if (*(arr + i) == false) return false;
	return true;
}
int main() {
	int TestCase;
	FILE *fs, *fp;
	fs = fopen("input.txt", "r");
	fp = fopen("output.txt", "w");
	fscanf(fs,"%d", &TestCase);

	for (int iterTest = 0; iterTest < TestCase; iterTest++) {
		bool check[10] = { 0, };
		int arr[100] = { 0, };
		int sum[100] = { 0, };
		int idx=-1;
		int n,t;

		fscanf(fs,"%d", &n);

		if (n == 0) {
			fprintf(fp,"Case #%d: INSOMNIA\n",iterTest+1);
			continue;
		}
		while (n > 0) {
			arr[++idx] = n % 10;
			n /= 10;
		}

		while (1) {
			for (int i = idx; i >-1; i--) {
				sum[i] += arr[i];
				t = 0;
				while(sum[i+t] > 9)
				{
					sum[i+t] -= 10;
					sum[i+t + 1]++;
					t++;
				}
			}
			if (sum[idx + 1] > 0)
				idx++;
			for (int i = 0; i <= idx; i++) {
				check[sum[i]] = true;
			}
			if (ch_num(check) == true) {
				fprintf(fp, "Case #%d: ", iterTest + 1);
				for (int i = idx; i > -1; i--)
					fprintf(fp,"%d",sum[i]);
				fprintf(fp,"\n");
				break;
			}
		}
	}
}