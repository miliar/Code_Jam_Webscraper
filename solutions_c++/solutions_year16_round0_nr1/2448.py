#include <iostream>

using namespace std;

int get_digit(long long N)
{
	int ret = 0;
	long long temp = N;
	int remaind;
	do {
		remaind = (int)(temp % 10);
		temp/=10;
		ret |= 0x1 << (remaind);
	} while(temp > 0);
	return ret;
}

long long get_test_num(int N)
{
	int index = 0;
	long long ret = 0, count = 1;
	int temp = 0;

	if (N >= 1) {
		do {
			ret = (long long)N * count;
			temp |= get_digit(ret);
			count++;
		} while(temp < 0x3FF);
	}
	return ret;
}

int main(void)
{
	int N, i;
	long long test[100];
	int temp;
	cin >> N;

	for(i=0; i<N; i++) {
		cin >> temp;
		test[i] = get_test_num(temp);
	}
	for(i=0; i<N; i++) {
		cout << "Case #" << (i+1) << ": ";
		if(test[i] == 0) {
			cout << "INSOMNIA";
		} else {
			cout << test[i];
		}
		cout << endl;
	}
}