#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <limits>

using namespace std;

string shrink(string input){
	string temp = "";
	temp += input[0];
	int counter = 0;
	for(int i = 1; i < input.length(); i++){
		if(input[i] != temp[counter]){
			temp += input[i];
			counter++;
		}
	}
	return temp;
}

/*string flip(string a, int n){
	string ret = a;
	for(int i = 0; i < n; i++){
		ret[i] = a[n-i-1] == '+' ? '-' : '+';
	}
	return ret;
}

long solve(string s){
	string temp = shrink(s);
	if(dp.find(temp) != dp.end()) return dp[temp]; //if we already know this temp 
	long m = 1000000;
	dp[s] = m;
	dp[temp] = m;
	for(int i = 1; i <= temp.length(); i++){
		long s = solve( flip(temp,i) ) + 1;
		if( m > s ) m = s;
	}
	dp[s] = m;
	dp[temp] = m;

	return m;
}*/
long solve(string input){
	int l = input.length();
	long counter = 1;
	for(int i = 0; i < l; i++){
		if(input[i] != input[i-1])
			counter++;
	}
	if(input[l-1] == '+')
		counter--;
	return counter - 1;
}

int main(){
	int R;
	cin >> R;
	string input;
	getline(cin,input);
	for(int i = 0; i < R; i++){
		getline(cin, input);
		cout << "Case #" << i+1 << ": " << solve(input) << endl;
	}
	return 0;
}
