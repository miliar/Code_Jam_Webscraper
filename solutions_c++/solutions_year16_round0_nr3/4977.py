#include <cstdio>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int input_n, input_j;
int base[9] = {2, 3, 4, 5, 6, 7, 8, 9, 10};

int isPrime(long long n) {
    for (long long i = 2; i * i <= n; i++) {
	if (n % i == 0) return i;
    }
    return -1;
}

string make_to_string(long long n) {

    string ret;
    for (int i = input_n-1; i >= 0; i--) {
	if (n & (((long long)1) << i)) {
	    ret += "1";
	} else {
	    ret += "0";
	}
    }
    return ret;
}

int main() {
    int TC;

    cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
	cin >> input_n >> input_j;
	int cnt = 0;

	long long start_candi = ((long long)1) << (input_n - 1);
	start_candi += (1<<0);

	printf("Case #1:\n");
	for (long long candi = start_candi; candi < (((long long)1)<<input_n); candi+=2) {
	    vector<long long> result;
	    for (int i = 0; i < 9; i++) {
		long long number = 0;
		for (int j = 0; j < input_n; j++) {
		    if (candi & (((long long)1)<<j)) {
			long long tmp = 1;
			for (int k = 0; k < j; k++) {
			    tmp *= base[i];
			}
			number += tmp;
		    }
		}
		long long divisor = isPrime(number);
		if (divisor == -1) break;
		result.push_back(divisor);

	    }
	    if (result.size() == 9) {
		string str_candi = make_to_string(candi);
		printf("%s ", str_candi.c_str());
		for (int i = 0; i < 9; i++) {
		    printf("%lld ", result[i]);
		}
		printf("\n");
		cnt++;
	    }
	    result.clear();
	    if (cnt == input_j) break;
	}

    }
    return 0;
}
