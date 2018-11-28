#include<iostream>
using namespace std;
int main(){
	int t, c;
	bool f;
	char s[128];
	cin >> t;
	for(int i = 0; i < t; i++){
		cin >> s;
		c = 0;
		f = false;
		for(int j = strlen(s)-1; j != -1; j--){
			if(f){
				if(s[j] == '+'){
					c++;
					f = false;
				}
			}else{
				if(s[j] == '-'){
					c++;
					f = true;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << c << '\n';
	}
	return 0;
}