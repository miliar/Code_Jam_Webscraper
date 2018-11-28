#include<iostream>
using namespace std;
int main(){
	int T; long long N, tempNum; unsigned int digitFlag = 0;
	cin >> T;
	for(int i=1; i<=T; i++){
		cin >> N;
		digitFlag = 0;
		if(N > 0){
			for(int j = 1; j <= 100000 ; j++){
				tempNum = N * j;
				while(tempNum > 0){
					int rem = tempNum % 10;
					tempNum = tempNum/10;
					digitFlag |= 1 << rem;
				}
				if(digitFlag == 1023){
					cout << "case #" << i << ": " << N * j << endl;
					break;
				}	
			}	
		}
		
		if(digitFlag != 1023){
			cout << "case #" << i << ": " << "INSOMNIA" << endl;
		}
	}
	return 0;
}
