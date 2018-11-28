#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

void printAnswer(int order, int answer) {
	cout << "Case #" << order << ": " << answer << endl;
}

int main() {
	int total_num;
	cin >> total_num;
	for(int m = 1; m <= total_num; m++) {
		string str;
		cin >> str;

		string tmp = str;

		int outer = 0;
		int inner = 0;

		int idx = 0;
		while(tmp[idx] == '-') {
			idx++;
		}

		if(idx != 0) outer = 1;

		for(int i = idx; i < tmp.size(); i++) {
			if(tmp[i] == '-') {
				inner += 2;
				while(tmp[i] == '-') {
					i++;
				}
			}
		}

		printAnswer(m, outer+ inner);
	}
}

