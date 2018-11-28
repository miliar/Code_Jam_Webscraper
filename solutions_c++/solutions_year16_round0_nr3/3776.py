#include<iostream>
#include<vector>
#include<string>
#include<stack>
using namespace std;

long long int TentoTwo(long long int num, int aa){
	long long int t = num;
	char a[40];

	int i = aa;
	while (t > 0){
		if (t % 2 == 0){
			a[i - 1] = '0';
		}
		else a[i - 1] = '1';
		t /= 2;
		i--;
	}

	return atoll(a);
}

int main(){

	int T;
	vector<long long int> myv;
	scanf("%d", &T);
	int a, b, t = 0;
	scanf("%d %d", &a, &b);
	//printf("%d %d %d\n", T, a, b);
	printf("Case #1:\n");
	for (int i = 32769; i <= 65535; i += 2){
		myv.clear();
		//printf("ok\n");
		long long int two = TentoTwo(i, a);
		int j;
		for (j = 2; j <= 10; j++){
			long long int k = 1;
			long long int tmp = two;
			long long int sum = 0;
			while (tmp > 0){
				long long int temp = tmp % 10;
				tmp /= 10;
				if (temp == 1){
					sum += k;
				}
				k *= j;
			}
			long long int kk;
			for (kk = 2; kk * kk <= sum; kk++){
				if (sum % kk == 0){
					myv.push_back(kk);
					break;
				}
			}
			
		}
		if (myv.size() == 9){
			printf("%lld ", two);
			for (int ii = 0; ii < myv.size(); ii++) printf("%lld ", myv[ii]);
			printf("\n");
			t++;
		}
		if (b == t) break;

	}
	return 0;
}