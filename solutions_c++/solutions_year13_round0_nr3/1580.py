#include <cstdio>
#include <stdlib.h>
#include <vector>

using namespace std;

long long inverse(long long n){
	long long k = 0;
	while (n){
		k = 10LL * k + n % 10LL;
		n /= 10LL;
	}
	return k;
}

bool isPalindrome(long long n){
	long long inv = inverse(n);
	while (n != 0){
		if (n % 10LL != inv % 10LL) return false;
		n /= 10LL;
		inv /= 10LL;
	}
	return true;
}

vector <long long> sol;

void bfSolve(int n){
	int ans = 0;
	for (int i = 1; i <= n; i++){
		long long k = i;
		if (isPalindrome(i) && isPalindrome(k*k)){
			sol.push_back(k*k);
		}
	}
}

int get(long long X){
	if (X == 0) return 0;

	int ans = 0;
	int left = 0, right = sol.size() - 1;
	while (left <= right){
		int j = left + right >> 1;
		if (sol[j] <= X){
			ans = j;
			left = j + 1;
		}
		else {
			right = j - 1;
		}
	}
	return ans + 1;
}

int get(long long A, long long B){
	return get(B) - get(A - 1);
}

int main(){
	FILE *fin = fopen("C.in", "r");
	FILE *fout = fopen("C.out", "w");

	int t;
	fscanf(fin, "%d", &t);

	bfSolve(10000000);

	for (int test = 1; test <= t; test++){
		long long A, B;
		fscanf(fin, "%I64d%I64d", &A, &B);
		fprintf(fout, "Case #%d: %d\n", test, get(A, B));
	}

	fclose(fin);
	fclose(fout);

//	system("pause");
	return 0;
}