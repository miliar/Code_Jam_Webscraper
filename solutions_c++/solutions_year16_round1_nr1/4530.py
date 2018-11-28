#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
/*
string foo(string S, string result){
	if(S == "")
		return "";
	string rec1 = result + S[0];
	string rec2 = S[0] + result;
	if(rec1 > rec2)
		return foo(S.substr(1, S.length() - 1), rec1); 
	else
		return foo(S.substr(1, S.length() - 1), rec2); 
}

int main() {
	int T; 
	cin >> T;
	int count = 1;
	while(count != T){
		string S;
		cin >> S;
		cout << "Case #" << count << ": " << foo(S, "") <<endl;
		count++;
	}
}
*/
int main() {
	int T; 
	cin >> T;
	int count = 0;
	while(count != T){
		string S;
		cin >> S;
		string result  = "";
		for(int i = 0; i < S.length(); i++){
			if(result + S[i] > S[i] + result){
				result = result + S[i];
			}
			else{
				result = S[i] + result;
			}
		}
		cout << "Case #" << count + 1 << ": " << result <<endl;
		count++;
	}
}