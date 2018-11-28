#include<iostream>
#include<stdlib.h>
#include<string>
using namespace std;
int main(){
	int T,K,C,S;
	cin >> T;
	for(int i = 0; i<T;i++){
		cin >> K;
		cin >> C;
		cin >> S;
		cout << "Case #"<< (i+1) << ":"; 
		for(int j=0; j < S;j++){
			cout << " " << j+1;
		} 
		cout << endl;
	}
}
