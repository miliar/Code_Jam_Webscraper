#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int main(){
	int ttCase;
	cin >> ttCase;
	int curr = 1;
	
	while(ttCase --){
		string currStr;
		cin >> currStr;
		cout << "Case #" << curr << ": ";
		int flip = 0;
		bool flipFlag = true;
		bool isFirst = true;
		for(int i=0;i<currStr.length();i++){
			//cout << endl << currStr[i] << " " <<flipFlag << " "<<flip;
			if(currStr[i] == '-'){
				if(flipFlag != false || isFirst){
					isFirst = false;
					flipFlag = false;
					flip++;
				}
				
			}
			else{
				if(flipFlag != true || isFirst){
					isFirst = false;
					flipFlag = true;
					flip++;
				}
			}
		}
		if(flipFlag){
			flip--;
		}
		//cout << endl;

		cout << flip << endl;
		curr++;
		
	}
}