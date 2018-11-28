#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <iostream>
#include <algorithm>
using namespace std;
long long size;
bitset<10000010> bs;
vector<int> primes;

void sieve(long long up_bnd)
{
	size = up_bnd + 1;
	bs.set(); bs[0] = bs[1] = 0;
	for(long long i = 2; i < size; i++){
		if(bs[i]){
			for(long long j = i * i; j <= size; j += i){
				bs[j] = 0;
			}
			primes.push_back((int)i);
		}
	}
}

bool isPrime(long long N)
{
	if(N <= size) return bs[N];
	for(int i = 0; i < (int)primes.size(); i++)
		if(N % primes[i] == 0) return false;
	return true;
}

int main() {
    int T, N, J, case_no = 1;
	cin >> T;
	sieve(10000000);
	while(T--){
		long long base_value = 0;
		cin >> N >> J;
		printf("Case #%d:\n", case_no++);
		for(long long i = (1 << (N - 1)) + 1; J != 0; i += 2){
			long long arr[9] = {0}, index = 0;
			for(int base = 2; base <= 10; base++){
				for(int j = 0; j < N; j++){
					if(i & (1 << j)){
						arr[index] += (long long)pow((double)base, j);
					}
				}
				base_value = arr[index];
				if(!isPrime(base_value)) index++;
				else break;
			}
			
			if(index == 9){
				J--;
				printf("%lld", arr[index - 1]);
				for(int i = 0; i < index; i++){
					long long div = 2, maxDiv = 0;
					for(; !maxDiv && div < arr[i]; div++)
						if(!(arr[i] % div))
							maxDiv = arr[i] / div;
					printf(" %lld", maxDiv);
				}
				printf("\n");
			}
		}
	}
    return 0;
}
