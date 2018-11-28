#include <iostream>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int j = 1; j <= t; j++){
		int a[10];
		for (int i = 0; i < 10; ++i){
				a[i] = 0;
		}		
		int count = 0;

		int num;
		cin >> num;
		if(num == 0)
			cout << "Case #" << j << ": " << "INSOMNIA" << endl;
		else{
			int i = 1;
			while(true){
				int temp = i*num;
				while(temp > 0){
					int last = temp%10;
					temp = temp/10;
					if(a[last] == 0)
						count++;
					a[last] = 1;
				}
				if(count == 10){
					cout << "Case #" << j << ": " << i*num << endl;
					break;
				}
				i++;
			}
		}
	}
}