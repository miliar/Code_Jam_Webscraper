#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void parse_num(int N, int* arr){
	int tmp = N;
	int digit;
	while(tmp){
		digit = tmp % 10;
		if(arr[digit] == 0)
			arr[digit] = N;
		tmp /= 10;
	}
}
int main(){
	int T;
	cin >> T;
	for(int T_i = 0; T_i < T; T_i++){
		int target = 0;
		int N;
		int arr[10] = {};
		cin >> N;
		if(N == 0){
			cout << "Case #" << T_i + 1 << ": INSOMNIA" << endl;
		}else{
			int i = 1;
			bool flag = true;
			while(flag){
				flag = false;
				parse_num(N * i++, arr);
				for(int j = 0; j < 10; j++){
					if(arr[j] == 0){
						flag = true;
						break;
					}
				}
			}
			for(int i = 0; i < 10; i++){
				if(target < arr[i])
					target = arr[i];
			}
			cout << "Case #" << T_i + 1 << ": " << target << endl;
		}
	}
	return 0;
}
