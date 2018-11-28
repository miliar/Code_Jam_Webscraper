#include <iostream>

using namespace std;

int arr[1005];

int main(){
	int t;
	int s;
	char dig;
	int p,ned;
	cin >> t;
	for(int i = 1 ; i <= t ; i++){
		p = 0;
		ned = 0;
		cin >> s;
		for(int j = 0 ; j <= s ; j++){
			cin >> dig;
			arr[j] = dig - '0';
		}

		for(int j = 0 ; j <= s ; j++){
			if(arr[j] != 0){
				if(p >= j){
					p += arr[j];
				}
				else{
					int temp = j - p;
					ned += temp;
					p += temp + arr[j];
				}
			}
		}

		cout << "Case #" << i << ": " << ned << endl;
	}

	return 0;
}