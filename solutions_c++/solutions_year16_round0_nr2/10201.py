#include<iostream>
#include<stdlib.h>
#include<string>
using namespace std;
int main(){
	int T;
	cin >> T;
	string pancakes;
	for(int i = 0; i<T;i++){
		cin >> pancakes;
		int count = 0;
		bool happy = true;
		string first = pancakes.substr(0,1);
		for(int iterator=0; iterator<pancakes.length(); iterator++){
			string current = pancakes.substr(iterator,1);
			if(current == "-" && happy == false){
				;
			}else if(current == "-" && happy== true){
				count++;
				happy = false;
			}else if(current == "+" && happy== true){
				;
			}else if(current == "+" && happy== false){
				happy = true;
			}
		}
		int num;
		if(count <= 0){
			num = 0;
		}else if(first == "-"){
			num = (count*2)-1;
		}else{
			num = (count*2);
		}	
		cout  << "Case #" << i << ": " << num << endl;
	}
}
