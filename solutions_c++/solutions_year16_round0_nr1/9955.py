#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int aZero(void);
int arr[10];
int main(void){
	int T;
	string temp = "";
	
	cin >> T;
	for(int i = 0; i < T; i++){

		fill_n(arr, 10, 0);
		long long n, ans;
		int index;
		cin >> n;
		ans = n;

		if(n == 0){
			cout << "Case #" << i+1 << ": INSOMNIA \n";
		}
		else{

			while(aZero()){
				temp = to_string(ans); // to_string
				for(long long k = 0; k < temp.length(); k++){
					index = (int) temp[k] - 48;
					if(arr[index] == 0){
						arr[index] = 1;
					}
				}
				ans += n;
			}

			ans -= n;
			cout << "Case #" << i+1 << ": " << ans << "\n";
		}
	}
}

int aZero(){
	for(int i = 0; i < 10; i++){
		if(arr[i] == 0)
			return 1;
	}
	return 0;
}
