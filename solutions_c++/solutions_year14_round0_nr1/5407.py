#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()
#define LL long long

using namespace std;

vector<int> getNumbers(){
	vector<int> res;
	int ans;
	cin >> ans;
	REP(y, 4){
		REP(x, 4){
			int value;
			cin >> value;
			if (y + 1 == ans)res.push_back(value);
		}
	}
	sort(ALL(res));
	return res;
}

int main(){
	int T;
	cin >> T;
	REP(testCase, T){
		vector<int> set1 = getNumbers();
		vector<int> set2 = getNumbers();
		vector<int> set3;
		set_intersection(ALL(set1), ALL(set2),back_inserter(set3));
		cout << "Case #" << testCase + 1 << ": ";
		if (set3.size() == 1){
			cout << (*set3.begin()) << endl;
		}
		else if (set3.size() == 0){
			cout << "Volunteer cheated!" << endl;
		}
		else{
			cout << "Bad magician!" << endl;
		}

	}
	return 0;
}