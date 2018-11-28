#include<cstdio>
#include<cmath>
#include<iostream>
#include<string>
#include<sstream>

using namespace std;

#define MAXT 1024


int main(){
	int T, N;
	cin >> T;
	for(int k=0; k<T; k++){
		cin >> N;
		int digit=0;
		
		cout << "Case #" << (k+1) << ": "; 
		if(N==0){ 
			cout << "INSOMNIA\n"; 
			continue;
		}

		int done=0;
		for(int i=1;!done;i++){
			ostringstream ss; 
			ss << (((long long)N) * i);
			string str = ss.str();
			for(int j=0; j<str.size(); j++){
				digit = digit | (1 << ((int)(str[j]-'0')));
				if(digit == 1023){
					cout << str << "\n";
					done=1;
					break;
				}
			}
		}
	}
}
