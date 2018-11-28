#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
	int numberOfTestCases;
	cin >> numberOfTestCases;
	
	for (int i =0; i <  numberOfTestCases;i++){
		int MaxShyness;
		string audience;
		int friends = 0;
		cin >> MaxShyness;
		cin >> audience;
		int stoodUp;
		stoodUp = audience.at(0) - 48 ;
		for(int j =1; j< MaxShyness +1; j++){
			do{
				if (stoodUp < j){
					stoodUp ++;
					friends ++;
				}else{
					stoodUp += audience.at(j) - 48;
					break;
				}
			}while(true);
		}
		
		int testCase = i+1;
		cout << "Case #" << testCase << ": " << friends << endl;
		
	}
	return 0;
}