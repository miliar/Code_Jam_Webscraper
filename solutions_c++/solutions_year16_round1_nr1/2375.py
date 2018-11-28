#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <math.h>
using namespace std;

int t;
string s;

string aiu(string s){
	string a = "";
	a = a + s[0];
	string b = "";
	for(int i = 1;i < s.size();i++){
		if(a[0] <= s[i]){
			b = s[i] + a;
			a = b;
		}else{
			b = a + s[i];
			a = b;
		}	
	}
	return a;
}

int main(void){
	cin >> t;
	for(int i = 0;i < t;i++){
		cin >> s;
		string result = aiu(s);
		cout << "Case #" << i+1 << ": " << result << endl;
	}
	return 0;
}
