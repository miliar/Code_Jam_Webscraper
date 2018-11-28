#include <iostream>

using namespace std;

int arr[30];

bool isNotEmpty(int n){
	for(int i = 0; i < n; i++){
		if(arr[i] != 0)
			return true;
	}
	return false;
}

int getLargest(int n){
	int result = 0;
	int val = arr[0];
	for(int i = 1; i < n; i++){
		if(arr[i] >= val){
			result = i;
			val = arr[i];
		}
	}

	return result;
}

int totalNum(int n){
	int result = 0;
	for(int i = 0; i < n; i++){
		result += arr[i];
	}
	return result;
}

int main(){

	int t;
	cin >> t;

	for(int i = 1; i <= t; i++){
		int n;
		cin >> n;
		for(int j = 0; j < n; j++){
			cin >> arr[j];
		}

		cout << "Case #" << i << ":";
		while(isNotEmpty(n)){
			if(totalNum(n) == 3 || totalNum(n) == 1){
				int res = getLargest(n);
				arr[res]--;
				cout << " " << (char)('A' + res);
			}
			else{
				int res1 = getLargest(n);
				arr[res1]--;
				int res2 = getLargest(n);
				arr[res2]--;
				cout << " " << (char)('A' + res1) << (char)('A' + res2);
			}
		}
		cout << endl;
	}

	return 0;
}