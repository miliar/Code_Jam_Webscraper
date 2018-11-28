#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int arr[10] = {0};

void getNStore (unsigned long long n) {
	while (n > 9) {
		arr[n%10]++;
		n /= 10;
	}
	arr[n]++;
}

int checkFreq (){
	int sum = 0;
	for (int i=0; i<10; i++) {
		if (arr[i] > 0)
			sum++;
	}
	if (sum == 10)
		return 1;
	else
		return 0;
}

void reset(){
	for (int i=0; i<10; i++)
		arr[i]=0;
}

int main(){
	int t, flag = 0;
	long long n;
	unsigned long long num;
	cin >> t;
	for (int i=1; i<=t; i++) {
		cin >> n;
		flag = 0;
		reset();
		if (n == 0)
			cout << "Case #"<<i<<": INSOMNIA"<<endl;
		else {
			for (int j = 1; flag != 1; j++) {
				num = n*j;
				getNStore (num);
				if (checkFreq())
					flag = 1;
			}
			//cout << flag << num <<endl;
			if (flag)
				cout << "Case #"<<i<<": "<<num<<endl;
		}
	}
	return 0;
}
