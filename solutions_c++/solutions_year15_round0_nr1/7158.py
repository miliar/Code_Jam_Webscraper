#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <memory.h>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int main() {
	long long maxsh,req_people = 0,standing_people = 0;
	string x;
	int tt;
	cin >> tt;
	for(int i=0;i<tt;i++) {
		cin >> maxsh >> x;
		standing_people = 0;
		req_people = 0;
		if((x[0] - '0') == 0) {
			req_people = req_people + 1;
			standing_people = standing_people + 1;
		} else {
			standing_people = standing_people + (x[0] - '0');
		}
		for(int sh_level=1;sh_level<=maxsh;sh_level++) {
			if(sh_level <= standing_people) {
				standing_people = standing_people + (x[sh_level] - '0');
			} else {
				req_people = req_people + (sh_level - standing_people);
				standing_people = sh_level + (x[sh_level] - '0');
			}
		}
		cout << "Case #"<<i+1<<":"<<" "<<req_people;
		if(i<tt-1) cout <<endl;


	}
	return 0;
}