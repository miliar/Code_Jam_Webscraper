#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main(void){
	string str;
	int block = 0, T, t = 1;
	
	cin >> T;
	while(T--){
		block = 0;
		cin >> str;
		if(str.length() == 1 && str[0] == '-') cout << "Case #" << t << ": 1" << endl;
		else if(str.length() == 1 && str[0] == '+') cout << "Case #" << t << ": 0" << endl;
		else {
			if(str[str.length() - 1] == '+'){
				for (int i = 0; i < str.length(); i++){
					if(str[i] != str[i + 1]) block++; 					
				}
				cout << "Case #" << t << ": " << max(0, block - 1) << endl;				
			} else {
				if(str[str.length() - 1] == '-'){
					for (int i = 0; i < str.length(); i++){
						if(str[i] != str[i + 1]) block++; 					
					}
					cout << "Case #" << t << ": " << block << endl;							
				}
			}
		}
		t++;	
	}

	return 0;
}