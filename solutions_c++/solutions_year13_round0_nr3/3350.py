//============================================================================
// Name        : GCJ2013_Q_3.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

std::vector<long> fairList;

int main() {
	int testcase_num = 0;
	std::cin >> testcase_num;

	fairList.push_back(1);
	fairList.push_back(4);
	fairList.push_back(9);
	fairList.push_back(121);
	fairList.push_back(484);

	sort(fairList.begin(), fairList.end());


	for(int i = 0; i < testcase_num; ++i){
		int a, b;
		cin >> a;
		cin >> b;

		vector<long> res;
		vector<long>::iterator itr = fairList.begin();
		for(; itr != fairList.end(); itr++){
			long x = *itr;
			if(a <= x && x <= b ){
				res.push_back(x);
			}
		}


		cout << "Case #" << i+1 << ": " << res.size() << endl;
	}

	return 0;

}
