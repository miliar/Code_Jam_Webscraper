#include <iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<stack>
#include<cstdint>
#include<bitset>
#include<map>
#include<unordered_map>
#include<queue>
#include<unordered_set>
#include <numeric>
#include <ctime>
using namespace std;

ofstream outs("res.txt");



int main() {
	
	int T, S, k;
	
	int shy[1005];
	int count = 0, sum;
	string str;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		count = 0;
		sum = 0;
		cin >> S;
		cin >> str;
		for (int j = 0; j <= S; j++) {
			if (sum >= j) {
				sum += str[j] - '0';
			}
			else {
				count += (j - sum);
				sum = j+str[j]-'0';
			}
		}

		outs << "Case #" << i << ": "<<count<<endl;
	}
	
	
	return 0;
}