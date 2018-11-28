#include <iostream>
#include <string>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int i=1;i<=T;i++){
		string s;
		cin >> s;
		int count = 0;
		char sign = s[0];
		for(int j=1;j<s.size();j++){
			if(s[j] == sign){
				continue;
			}else{
				count++;
				sign = s[j];
			}
		}
		if(sign == '-')count++;
		cout << "Case #" << i << ": " << count << "\n";
	}
}
