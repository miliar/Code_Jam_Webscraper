#include<iostream>
#include<string>
#include<sstream>
#include<math.h>
using namespace std;
void flip(char seq[], int f){
	for(int i = 0; i< f; i++){
		if(seq[i] == '+'){
			seq[i] = '-';
		}else{
			seq[i] = '+';
		}
	}
}
int main(){
	int t;
	
	cin >> t;
	
	for(int i = 0; i < t; i++){
		char seq[101] = "";
		cin >> seq;
		int iter = 0;
			while(true){
				
				if(seq[iter] == '\0'){
					break;
				
				}
				iter++;
				
			}
		int len = iter;
			
		int flips = 0;
		while(true){
			int min_sign = -1;
		
	
			int mc = 0;
			for(int a = 0; a< len; a++){
				if(seq[a] == '-'){
					min_sign = a;
					mc++;
				}
				if(seq[a] == '\0'){
					break;
				
				}
				iter++;
				
			}
			
			// check if all happy 
			
			if(min_sign != -1){
				flips++;
				flip(seq, (min_sign+1));
			}else{
				cout << "Case #"<<(i+1)<<": "<<flips << endl;
				break;
			}
		}
		
	}
	return 0;
}