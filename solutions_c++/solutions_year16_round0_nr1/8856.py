#include <bits/stdc++.h>

using namespace std;

int main(){
	int i, j;
	int t;
	unsigned long n;
	int digit[10] = {0};
	int total = 0;
	cin >> t;
	for (i = 0; i < t; i++){
		cin >> n;
		for (j = 1; total != 10 && n != 0; j++){
			int num;
			num = n*j;
			//cout << num << endl;
			while (num > 0){
				int rem = num%10;
				if (digit[rem] == 0){
					digit[rem] = 1;
					total++;
				}
				num /= 10;
			}
		}
		cout << "Case #" << i+1 << ": ";
		if (n == 0)
			cout << "INSOMNIA" << endl;
		else 
			cout << n*(j-1) << endl;

		total = 0;
		for (j = 0; j < 10; j++){
			digit[j] = 0;
		}
	}
	return 0;
}