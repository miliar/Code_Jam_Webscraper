#include <bits/stdc++.h>

using namespace std;

int main(){
	long long int test, n, flag;
	int d;
	cin >>test;
	for (long long int tt=1; tt<=test; tt++) {
		cin >> n;
		long long int num = 0;
		flag = 0;
		bool digits[10];
		for (int i=0; i<10; i++) digits[i] = false;
		int count = 0;
		for (int i=0; i<=10000000; i++) {
			num += n;
			// printf("%lld\n", num);
			int temp = num;
			while (temp!=0) {
				d = temp%10;
				if (digits[d] == false) {
					// printf("-------Digit: %d\n", d);
					digits[d] = true;
					count++;
				}
				temp = temp/10;
			}
			if (count == 10) { 
				flag = 1;
				break;
			}
		}
		if (flag != 0)
			printf("Case #%lld: %lld\n",tt, num);
		else
			printf("Case #%lld: INSOMNIA\n", tt);
	} 
	return 0;
}