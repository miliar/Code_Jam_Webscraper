#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#include <stack>

using namespace std;


int main() {

	int t;
	cin >> t;

	for (int k = 1; k <= t; k++){

		string str;
		cin >> str;

		int count = 0;

		if (str[str.size() - 1] == '-')
				count++;

		for (int i = 0; i < str.size() - 1; i++){
			if (str[i] != str[i + 1]){
				count++;
			}
		}

		cout << "Case #" << k << ": "  << count << endl;

	}

	return 0;
}