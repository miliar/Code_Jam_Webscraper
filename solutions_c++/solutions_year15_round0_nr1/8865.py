#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main(){
	int T, Smax, cont, lastPosition, currentPosition, cases = 1;
	string input;
		cin >> T;
	while (T--){
		lastPosition = currentPosition = cont = 0;
		cin >> Smax;
		cin >> input;
		//use for not get a same value
		bool *verifyPosition = new bool[input.size()]();
		//Case Smax = 0
		if (Smax == 0 && input != "0"){
			cout << "Case #" << cases << ": 0" << endl;
			cases++;
			continue;
		}
		//Another cases
		while (currentPosition < Smax){
			// if current position is equal a zero and last position and current positon is a same
			if ((lastPosition == currentPosition) && (input[currentPosition] == '0')){
				verifyPosition[currentPosition] = true;
				cont++;
				currentPosition++;
				lastPosition = currentPosition;
				continue;
			}
			//case te current position is not equal to zero 
			if (input[currentPosition] != '0') {
				verifyPosition[currentPosition] = true;
				currentPosition += input[currentPosition]-'0';
				continue;
			}
			//if current position is equal to a zero
			if (input[currentPosition] == '0'){
				if (verifyPosition[lastPosition]){
					lastPosition++;
				}
				else{
					verifyPosition[lastPosition] = true;
					currentPosition += input[lastPosition] - '0';
					lastPosition++;
				}
			}
		}
		cout << "Case #" << cases << ": " << cont << endl;
		cases++;
	}
	return 0;
}