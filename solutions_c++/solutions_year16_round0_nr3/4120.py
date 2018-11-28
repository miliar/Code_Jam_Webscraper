#include<stdio.h>
#include<string.h>
#include<vector>
#include<math.h>
#define MAX_CHK 44721360
bool chkPrime[MAX_CHK] = { true, true, false, };
std::vector<int> prime;
void solutionSmall(int n, int j) {
	long long int num = 1;
	for (int i = 1; i < n; i++) num *= 10;
	num++;
	long long int max = (num - 1) * 2;
	for (; num < max; num += 10) {

		{
			long long int plus = 1;
			while (plus < num / 10) {
				plus *= 10;
				if (1 < (num / plus) % 10) num += (10 - (num/plus)%10)*plus;
				if (max <= num) break;
			}
		}
		if (max <= num) break;

		long long int save[11];
		bool chk = true;
		for (int i = 2; i <= 10; i++) {
			long long int tmp = num;
			long long int tNum = 0;
			long long int p = 1;
			while (tmp) {
				tNum += (tmp % 10)*p;
				p *= i;
				tmp /= 10;
			}
			bool fail = true;
			long long int tSqrt = (long long int)sqrt((double)tNum);
			for (int l = 0; l < prime.size(); l++) {
				if (tSqrt < prime[l]) break;
				if (tNum % prime[l] == 0) {
					fail = false;
					save[i] = prime[l];
					break;
				}
			}
			if (fail) {
				chk = false;
				break;
			}
		}
		if (chk) {
			printf("%lld", num);
			for (int i = 2; i <= 10; i++) {
				printf(" %lld", save[i]);
			}
			printf("\n");
			j--;
			if (!j) break;
		}
	}
}
int main() {
	prime.push_back(2);
	for (int i = 4; i < MAX_CHK; i += 2) 
		chkPrime[i] = true;
	for (int i = 3; i < MAX_CHK; i += 2) {
		if (!chkPrime[i]) {
			prime.push_back(i);
			for (int l = i * 2; l < MAX_CHK; l += i)
				chkPrime[l] = true;
		}
	}
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc; scanf("%d\n", &tc);
	for (int test = 1; test <= tc; test++) {
		int n, j; scanf("%d %d", &n, &j);
		printf("Case #%d:\n", test);
		if (n <= 16) solutionSmall(n, j);

	}
	fclose(stdin);
	fclose(stdout);
}