#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
using namespace std;

void main(){
	freopen("input.in", "r", stdin);
	freopen("input.out", "w", stdout);
	int n,val;
	string s;
	cin >> n;
	for (int i = 0; i < n; i++){
		cin >> val;
		cin >> s;
		int sum = 0;
		val = 0;
		for (int j = 0; j < s.size(); j++){
			
			if (sum < j){
				val += j- sum;
				sum += j -sum;
			}
			sum += s[j] - '0';

		}
		cout << "Case #" << i + 1 << ": " << val<<"\n";
	}

}