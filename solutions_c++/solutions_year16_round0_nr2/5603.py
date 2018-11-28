#include <iostream>
using namespace std;

int t;
char arr[101] = { '0', };

int chkResult(int cc){
	int chk = 0;
	for (int i = 0; i < cc; i++){
		if (arr[i] == '+'){
			chk++;
		}
	}
	if (chk == cc){
		return 1;
	}
	else{
		return 0;
	}

}

int main(){

	cin >> t;

	for (int a = 1; a <= t; a++){
		cout << "Case #" << a << ": ";
		cin >> arr;
		int cnt = 0;
		for (int i = 0; arr[i] != NULL; i++){
			cnt++;
		}
		int result = 0;
		while (1){
			if (chkResult(cnt)){
				cout << result << endl;
				break;
			}

			char first_c = arr[0];
			int temp = 0;
			for (int i = 0; i<cnt && first_c == arr[i]; i++){
				temp++;
			}
			for (int i = 0; i < temp; i++){
				if (arr[i] == '-'){
					arr[i] = '+';
				}
				else if (arr[i] == '+'){
					arr[i] = '-';
				}
			}
			result++;
		}
		for (int i = 0; i<101; i++){
			arr[i] = '0';
		}
	}

	return 0;
}