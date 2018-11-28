#include<iostream>
#include<vector>
using namespace std;


int main(){
	int tn;
	int n, max, res;
	cin >> tn;
	int A[1000];
	for (int ti = 0; ti < tn; ti++){
		cin >> n;
		max = 0;
		res = 1000;
		for (int i = 0; i < n; i++){
			cin >> A[i];
			if (A[i] > max)
				max = A[i];
		}
		for (int i = 1; i <= max; i++){ // delenia
			int specNum = 0;
			for (int j = 0; j < n; j++)
				specNum += ceil((double(A[j]) / i)) - 1;
			if (res > specNum + i)
				res = specNum + i;
		}
		printf("Case #%d: %d\n", ti + 1, res);
	}

	return 0;
}