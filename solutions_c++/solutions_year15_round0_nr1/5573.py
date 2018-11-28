#include <iostream>
#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cstring>
#include <functional>
#include <list>
#include <map>
#include <numeric>
#include <stack>
#include <string>
#include <vector>
#include <queue>
#include <fstream>

using namespace std;

const string fileName = "StandingOvation";

int s_max;
string digits;

int main(){
	ofstream file(fileName + ".txt", ofstream::out);

	int testCase;
	cin >> testCase;
	for (int t = 0; t < testCase; t++){
		cin >> s_max >> digits;

		int clapPersonCount = 0;
		int friendCount = 0;
		for (int i = 0; i < s_max + 1; i++){
			char ch=digits[i];
			int s_i = atoi(&ch);

			if (i > clapPersonCount){
				int needFriendCount = i - clapPersonCount;
				friendCount += needFriendCount;
				clapPersonCount += needFriendCount;
			}
			clapPersonCount += s_i;
		}

		file << "Case #" << (t + 1) << ": " << friendCount<< endl;
	}

	file.close();
	return 0;
}