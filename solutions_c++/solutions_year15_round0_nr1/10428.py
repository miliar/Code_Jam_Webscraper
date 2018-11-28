#include <iostream>
#include <string>
// #include <fstream>
using namespace std;

string process(int ci, int si, string &s){
	int result = 0;
	int curSum = 0;
	for(int i = 0; i <= si; i++){
		if(i > curSum){
			int gap = i - curSum;
			result += gap;
			curSum += (gap+(s[i]-'0'));
		}else{
			curSum += (s[i]-'0');
		}
		if(curSum > si) break;
	}
	return "Case #"+to_string(ci+1)+": "+to_string(result);
}

int main(){
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int si;
		string s;
		cin >> si >> s;
		cout << process(i, si, s)<<"\n";
	}
	return 0;
}