#include <vector>
#include <list>
#include <map>
#include <set>
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
 
 
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for (int i = 0; i<cases; i++){
		printf("Case #%d: ", i+1);
		fflush(stdout);
		int maxShyness;
		string totalPeople;
		cin >> maxShyness >> totalPeople;
		int friends=0,people = 0;
		for (int i = 0; i<maxShyness; i++){
			int current = totalPeople[i] - '0';
			people += current;
			while (people<(i + 1)){
				friends++;
				people++;
			}
			
		}
		cout << friends << endl;
		fflush(stdout);
	}
	return 0;
}