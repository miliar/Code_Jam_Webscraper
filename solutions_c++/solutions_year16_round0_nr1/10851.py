#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int main() {
	int array1[100];
	int array2[100];
	int N = 0;
	int number = 0;
	int s = 0;
	int t = 0;
	int m = 1;
	memset(array1, 0, sizeof(array1));
	memset(array2, 0, sizeof(array2));
	cin >> s;
	while (s--) {
		cin >> number;
		int count = 0;
		N = number;
		t = number;
		while (number) {
			for (int i = 0; i <= 20; i++) {
				if (number % 10 == 0 && number / 10 == 0)
					break;
				array1[i] = number % 10;
				if (array2[array1[i]] == 0) {
					array2[array1[i]] = 1;
					count++;
					if (count == 10)
						break;
				}
				number = number / 10;
			}
			memset(array1, 0, sizeof(array1));
			N += t;
			number = N;
			if (count == 10)
				break;
		}
		if (number != 0)
			cout << "Case #" << m << ": " << N - t << endl;
		else
			cout << "Case #" << m << ": " << "INSOMNIA " << endl;
		memset(array1, 0, sizeof(array1));
		memset(array2, 0, sizeof(array2));
		m++;
	}
	//system("pause");
	return 0;
}
