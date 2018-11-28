#include <iostream>
#include <algorithm>
#include <string>
#include <math.h>
using namespace std;

bool is_ok(string a){
	for(char c : a){
		if(c != '+') return false;
	}
	return true;
}

int main(void){
	int t;
	string cake;
	cin >> t;
	for(int i = 0;i < t;i++){
		cin >> cake;
		int turn = 0;
		while(!is_ok(cake)){
			if(cake[0] == '+'){
				cake.replace(0, cake.find('-')+1, cake.find('-')+1, '-');
			}else{
				if(cake.find('+') == string::npos){
					turn++;
					break;
				}
				int rev_num = cake.find('+');
				string tmp = cake.substr(rev_num, cake.size()-rev_num);
				cake.replace(0, cake.size()-rev_num, tmp);
				cake.replace(cake.size()-rev_num, rev_num, rev_num, '+');
			}
			turn++;
		}
		cout << "Case #" << i+1 << ": " << turn << endl;
	}
	return 0;
}
