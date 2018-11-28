#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <limits>
#include <utility>
#include <functional>
#include <iostream>
#include <sstream>
#include <cctype>
#include <cmath>
//#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
//using namespace boost::multiprecision;

string getTemplate(const string &s){
	string res;
	char prev = '\0';
	for (char c : s){
		if (c != prev){
			res += c;
			prev = c;
		}
	}
	return res;
}

vector<int> getCounts(const string &s){
	vector<int> res;
	char prev = '\0';
	for (char c : s){
		if (c != prev){
			res.push_back(1);
			prev = c;
		}
		else{
			res.back()++;
		}
	}
	return res;
}

void comp(int tc){
	int N;
	cin >> N;
	vector<vector<int>> v;
	string tmpl;
	for (int i = 0; i < N; ++i){
		string s, curTmpl;
		cin >> s;
		curTmpl = getTemplate(s);
		if (i == 0)
			tmpl = curTmpl;
		else if (tmpl != curTmpl){
			cout << "Case #" << tc << ": Fegla Won" << endl;
			return;
		}		

		v.push_back(getCounts(s));		
	}

	int n = (int)tmpl.size();
	int res = 0;
	for (int i = 0; i < n; ++i){
		int best = numeric_limits<int>::max();
		for (int target = 1; target <= 100; ++target){
			int cur = 0;
			for (int j = 0; j < N; ++j){
				cur += abs(target - v[j][i]);
			}
			best = min(best, cur);
		}
		res += best;
	}

	cout << "Case #" << tc << ": " << res << endl;

}

int main(){
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc){
		comp(tc);
	}
}