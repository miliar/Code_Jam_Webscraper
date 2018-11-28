#include <iostream>
using namespace std;

int main(){
	int testCases;	
	cin >> testCases;
	for(int i = 0; i < testCases; i++){
		int teller = 0;
		int go = 0;
		int sMax = 0;
		cin >> sMax;
		char temp[sMax+1];
		for(int j = 0; j < sMax+1; j++){
			cin >> temp[j];
		}
		for(int j = 0; j < sMax+1; j++){
			int konV = temp[j] - '0';
			
			if(go < j){
				teller += j-go;
				go = j;

			}
			go += konV;


		}
		

		cout << "Case #" << i+1 << ": " << teller << endl;


	}
	return 0;

}
