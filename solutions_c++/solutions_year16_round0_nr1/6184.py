#include <iostream>
using namespace std;

int main(){
	int t;
	cin >> t;
	int index = 1;
	while(t--){
		int n;
		cin >> n;

		if(!n){
			cout << "Case #" << index << ": INSOMNIA" << endl;
			index++;
			continue;
		}

		int h[10] = {0};
		int delta = n;
		int flag = true;

		while(1){

			int out = true;
			for(int i = 0;i < 10;i++){
				if(h[i] == 0){
					out = false;
					break;
				}
			}

			if(out){

				if(!flag){
					n = n - delta;
				}
				cout << "Case #" << index << ": " << n << endl;
				index++;
				break;
			}
			else{

				flag = false;
				
				int temp = n;
				while(temp != 0){
					int r = temp % 10;
					h[r] = 1;
					temp = temp / 10;
				}
				n = n + delta;
			}
		}
	}
	return 0;
}