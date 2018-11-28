//============================================================================
// Name        : codejam-C-simple.cpp
// Author      : myscloud
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector< pair<int, vector<int> > > number;
int start = 32769;
int stop = 65536;
int limit = 50;

string toBase2(int x){
	string text = "";
	while(x > 0){
		text += char((x%2) + 48);
		x /= 2;
	}
	string reverse = "";
	for(int i = text.length()-1; i >= 0; i--){
		reverse += text[i];
	}
	return reverse;
}

int main() {
	for(int num = start; num < stop; num+=2) {
		vector<int> divide(11, 0);
		int count = 0;
		for(int i = 2; i <= 10; i++) {
			long long inbase = 0;
			if(i == 2) inbase = num;
			else{
				int tmpnum = num;
				long long mul = 1;
				while(tmpnum > 0) {
					int mod = tmpnum % 2;
					inbase += (mod * mul);
					mul *= i;
					tmpnum /= 2;
				}
			}

			if(inbase % 2 == 0) divide[i] = 2;
			else{
				for(int j = 3; j < 100000000 && j < inbase; j+=2){
					if(inbase % j == 0){
						divide[i] = j;
						break;
					}
				}
			}
			if(divide[i] != 0) count++;
		}
		if(count == 9){
			number.push_back(std::make_pair(num, divide));
		}
		if(number.size() == limit) break;
	}
	cout << "Case #1:" << endl;
	for(int i = 0; i < number.size(); i++){
		cout << toBase2(number[i].first) << " ";
		for(int j = 2; j <= 10; j++) cout << number[i].second[j] << " ";
		cout << endl;
	}
	return 0;
}
