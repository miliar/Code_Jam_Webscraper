#include <iostream>
using namespace std;

int t;
int arr[10] = { 0, };

int chkAll(){
	int aa = 0;
	for (int i = 0; i < 10; i++){
		if (arr[i] == 1){
			aa++;
		}
	}
	if (aa == 10){
		return 1;
	}
	else{
		return 0;
	}

}

int main(){

	cin >> t;
	int n;

	for (int a = 1; a <= t; a++){
		cout << "Case #" << a <<": ";
		cin >> n;
		int cnt = 0;
		int idx = 1;
		int result = 0;
		if (n == 0){
			cout << "INSOMNIA" << endl;
		}
		else{
			int temp = n;
			while (1){
				while (1){
					arr[temp % 10] = 1;
					temp = temp / 10;
					if (temp == 0){
						break;
					}
				}
				if (chkAll()){
					cout << result << endl;
					break;
				}
				idx++;
				temp = n * idx;
				result = temp;
			}
		}
		for (int i = 0; i < 10; i++){
			arr[i] = 0;
		}
	}
	return 0;
}