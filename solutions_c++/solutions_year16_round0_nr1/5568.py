#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <bitset>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    long long T, N, case_no = 1, value;
	cin >> T;
	while(T--){
		long long i = 1, temp, size = 0;
		bitset<10> bits; 
		bool flag = false;
		cin >> N;
		value = 0;
		while(1){
			temp = value = i * N;
			if(value == 0) break;
			while(temp){
				bits.set(temp % 10);
				temp /= 10;
			}
			size = 0;
			for(size_t n = 0; n < bits.size(); n++){
				if(bits.test(n)) size++;
			}
			if(size == bits.size()) {flag = true; break;}
			i++;
		}
		printf("Case #%d: ", case_no++);
		if(!flag) printf("INSOMNIA\n");
		else printf("%d\n", value);
	}
    return 0;
}
