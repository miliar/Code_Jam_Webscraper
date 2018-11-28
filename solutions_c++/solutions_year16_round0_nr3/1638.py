#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;
int N, J;

int main(){
	cin >> N >> N >> J;
	if(N == 16){
		cout << "Case #1:" << endl;
		int i = 2, j = 2, k = 2;
		for(int zz = 0; zz < J; zz++){
			while(true){
				if(j > 12){
					i++;
					j = 2;
					k = 2;
				}
				else if(k > 12){
					j++;
					k = 2;
				}
				else if(j-i < 2)
					j++;
				else if(k-j < 2)
					k++;
				else{
					break;
				}
			}
			string str = "1100000000000011";
			str[i] = str[i+1] = str[j] = str[j+1] = str[k] = str[k+1] = '1';
			cout << str << " 3 4 5 6 7 8 9 10 11" << endl;
			k++;
		}
	}
	else{
		cout << "Case #1:" << endl;
		int i = 2, j = 2, k = 2;
		for(int zz = 0; zz < J; zz++){
			while(true){
				if(j > 28){
					i++;
					j = 2;
					k = 2;
				}
				else if(k > 28){
					j++;
					k = 2;
				}
				else if(j-i < 2)
					j++;
				else if(k-j < 2)
					k++;
				else{
					break;
				}
			}
			string str = "11000000000000000000000000000011";
			str[i] = str[i+1] = str[j] = str[j+1] = str[k] = str[k+1] = '1';
			cout << str << " 3 4 5 6 7 8 9 10 11" << endl;
			k++;
		}
	}
}