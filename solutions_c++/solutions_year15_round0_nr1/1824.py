#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int result(vector<int> v) {
    int res = 0;
    int cur = 0;
    for(int i = 0; i < (int)v.size(); i++) {
	if(i > cur) {
	    res += i-cur;
	    cur = i;
	}
	cur += v[i];
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
	int maxS;
	cin >> maxS;
	cin.ignore();
	string s;
	cin >> s;
	vector<int> v;
	for(int i = 0; i < (int)s.size(); i++) {
	    v.push_back(s[i]-'0');
	}
	cin.ignore();
	cout << "Case #" << t+1 <<": " << result(v) << endl;
    }
    return 0;
}
