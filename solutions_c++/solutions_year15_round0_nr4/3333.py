#include<iostream>
using namespace std;

int main() {
	int s;
	cin >> s;
	string str1 = "GABRIEL";
	string str2 = "RICHARD";
	for(int i = 0; i < s; i++){
		int x, r, c;
		cin >> x;
		cin >> r;
		cin >> c;
		int rc = r * c;
		cout << "Case #" << i+1 << ": ";
		if(x == 1){
			cout << str1 << endl;
		}
		if(x == 2){
			if( (r * c) % 2 == 0){
				cout << str1 << endl;
			} else {
				cout << str2 << endl;
			}
		}
		if(x == 3) {
			if (rc == 6 || rc == 12 || rc == 9){
				cout << str1  << endl;
			}else {
				cout << str2 << endl;
			}
		}
		if(x == 4){
			if(rc == 12 || rc == 16){
				cout << str1 << endl;	
			} else {
				cout << str2 << endl;
			}
		}
	}
}
