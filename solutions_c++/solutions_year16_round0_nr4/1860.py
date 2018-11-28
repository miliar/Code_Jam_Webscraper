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
	cout << "Case #" << order << ": ";

	for(int i = 1; i <= answer; i++) {
		cout << i;
		if(i != answer)
			cout << " ";
	}
	cout << endl;

}

int main() {
	int total_num;
	cin >> total_num;
	for(int m = 1; m <= total_num; m++) {
		int K, C, S;
		scanf("%d %d %d", &K, &C, &S);

		printAnswer(m, K);
	}
}

