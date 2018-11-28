#include <iostream>

using namespace std;

int main(){
	long long num, count,temp, len,cur;
	int arr[10];
	cin >> count;
	for(int i = 1 ; i <= count ; i++){
		cin >> num;
		if(num == 0){
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}
		arr[0] = arr[1] = arr[2] = arr[3] = arr[4] = arr[5] = arr[6] = arr[7] = arr[8] = arr[9] = 0;
		len = 0;
		for(int j = 1 ; j < 1000 ; j++){
			cur = temp = j * num;
			do{
				if(arr [ temp % 10 ] == 0){
					len++;
				}
				arr[ temp % 10 ]++;
				temp = temp / 10;
			}while(temp > 0);
			
			if(len >= 10){
				cout << "Case #" << i << ": " << cur << endl;
				break;
			}
		}
	}

	return 0;
}

int division(){
	int target;

	return target;
}