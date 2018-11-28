#include <iostream>
#include <string>
using namespace std;

int main(){

	int t ;

	cin >> t;

	for(int tt=1;tt<=t;tt++){

		int n;
		string num;

		cin >> n;
		cin >> num;

		n+=1;
		int arr[n];

		for(int i=0;i<n;i++){
			arr[i] = num[i] - '0';
			//cout << arr[i] << " ";
		}

		//cout << endl;
		int cur  = 0;
		int ans = 0;
		for(int i=0;i<n;i++){
			if(arr[i] == 0){
				continue;
			}
			if(cur < i){
				//cout << cur << endl;
				ans += (i - cur);
				cur = i;
			}

			cur += arr[i];
		}

		cout << "Case #" << tt << ": " << ans << endl;
	}
}