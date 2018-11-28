//============================================================================
// Name        : GCJ2013_C_1.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> vec;

bool isVowel(const char c){
	if(c == 'a' || c == 'i' || c == 'u' || c == 'e' || c == 'o'){
		return true;
	}
	return false;
}
int solve(int n){
	int count = 0;

	int length = vec.size();

//	for(int i = 0; i < length; i ++){
//		cout << vec[i] << endl;
//	}

	int blockNum = 0;
	int consNum = 0;
	int lastIdx = 0;
	for(int i = 0; i < length; i++){
		//cout << "vec["<< i << "]: " << vec[i] << endl;
		// nこ続いているのを探す
		if(vec[i] == 1){
			consNum++;
		}else{
			consNum = 0;
		}
		if(consNum == n){
			//cout << "cons! " << (i - n + 2 - lastIdx) << " x " << (length - i) << ":" << (i - n + 2 - lastIdx) * (length - i) << endl;
			count += (i - n + 2 - lastIdx) * (length - i);
			blockNum++;

			// consNum
			consNum -= 1;
			lastIdx = i - n + 2;
		}
	}
	//cout << "count:" << count << endl;
	//cout << "block:" << blockNum << endl;

	//count -= blockNum - 1;
	return count;
}
int main() {
	int testcase_num = 0;
	std::cin >> testcase_num;


	for(int i = 0; i < testcase_num; ++i){
		vec.clear();
		string name;
		cin >> name;

		for(int j = 0; j < (int)name.size(); j++){
			if(isVowel(name.at(j))){
				vec.push_back(0);
			}else{
				vec.push_back(1);
			}
		}

		int n = 0;
		cin >> n;

		int ans = solve(n);

		cout << "Case #" << i+1 << ": " << ans << endl;
	}

	return 0;
}
