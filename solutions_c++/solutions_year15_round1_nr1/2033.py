#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int rat(int inp[], int size){
	int rate = 0;
	for(int i = 1; i<size; i++){
		if(inp[i]<inp[i-1]){
			if(rate < (inp[i-1] - inp[i])){
				rate = inp[i-1] - inp[i];
			}
		}
	}
	return rate;
}

int meth1(int inp[], int size){
	long long int sum = 0;
	for(int i = 1; i<size;i++){
		if(inp[i] <= inp[i-1]){
			sum += (inp[i-1] - inp[i]);
			// cout << sum << endl;
		}

	}
	return sum;
}

int meth2(int inp[], int size){
	int rate = rat(inp,size);
	long long int sum = 0;
	for(int i = 1; i<size;i++){
		// if((inp[i-1]-inp[i]) > rate){
		// 	sum += rate;
		// }
		// else if((inp[i-1] - inp[i]) > 0){
		// 	sum += (inp[i-1] - inp[i]);
		// }
		// else {
		// 	sum += inp[i-1];
		// }
		if((inp[i-1])> rate){
			sum += rate;
		}
		else {
			sum += inp[i-1];
		}
	}
	return sum;
}

int main(){
	int t;
	cin >> t;
	int i = 1;
	while(t--){
		int n;
		cin >> n;
		int inp[n];
		for(int j = 0;j<n;j++){
			cin >> inp[j];
		}
		// for(int h = 0; h<n;h++){
		// 	cout << inp[h];
		// }
		cout << endl;
		long long int m1 = meth1(inp,n);
		long long int m2 = meth2(inp,n);

		cout << "Case #"  << i << ": " << m1 << " " << m2 << endl;

		i++;
	}
	return 0;
}