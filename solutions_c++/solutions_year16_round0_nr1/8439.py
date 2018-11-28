#include <iostream>
#include <cstdio>
using namespace std;

long long getAns(int N) {
	long long temp;
	int i;
	int flag;
	int arr[10] = {0};
	for(i = 1; ; ++i) {
		temp = i * N;
		do {
			arr[temp%10]++;
			temp /= 10;
		}while(temp);

		flag = 1; //Assume first all array elements are atleast 1

		for(int j = 0; j < 10; j++)
			if(arr[j] == 0) flag = 0;

		if(flag) break;
	}
	return i * N;
}

int main() {
	int T;
	cin >> T;
	int N;
	for(int i = 1; i <= T; i++) {
		cin >> N;
		if(N == 0)
			printf("Case #%d: INSOMNIA\n", i);
		else
			printf("Case #%d: %lld\n", i, getAns(N));
	}

return 0;
}