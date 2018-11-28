#include <string>
#include <iostream>
#include <list>
#include <map>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <math.h>

using namespace std;

int main() {

	int T, SMax;
	string shynessVal;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin>>T;

	for (int i=1;i<=T;++i) {
		cin>>SMax>>shynessVal;
		long long int minNoOfFriends = 0;
		long long int temp = 0;

		for (int j=0;j<shynessVal.size();++j) {
			int digit = shynessVal[j] - '0';
			if (digit != 0)
				minNoOfFriends += (temp+minNoOfFriends < j ? j-temp-minNoOfFriends : 0);
			temp += digit;
		}

		cout<<"Case #"<<i<<": "<<minNoOfFriends<<endl;
	}

	return 0;
}
