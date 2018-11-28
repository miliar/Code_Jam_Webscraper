#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <cstring>

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int test = 0; test < T; test++){
		long long N;
		scanf("%lld", &N);
		if (N == 0)
			printf("Case #%d: INSOMNIA\n", test + 1);
		else{
			long long number = N;
			bool digits[10];
			memset(digits, false, sizeof digits);
			int count = 0;
			while (true){
				long long temp = number;
				while (temp > 0){
					int digit = temp % 10;
					temp /= 10;
					if (!digits[digit]){
						digits[digit] = true;
						count++;
						if (count == 10)
							break;
					}
				}
				if (count == 10)
					break;
				number += N;
			}
			printf("Case #%d: %lld\n", test + 1, number);
		}
	}
}
