#include <iostream>
#include <stack>
#include <queue>
#include <bitset>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <functional>
#include <utility>
#include <sstream>
#include <iomanip>
#include <ctime>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
using namespace std;

/*

*/

int run() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<int> v;
    for (int i = 0; i < s.size(); i++) {
        v.push_back(s[i] - '0');
    }
    int res = 0;
    int cur = 0;
    for (int i = 0; i < v.size(); i++) {
        if (cur < i) {
            res += i - cur;
            cur = i;
        }
        cur += v[i];
    }
    return res;
}


int main(int argc, char *argv[]) {
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
			
	int t;
	cin >> t;
	int k = 0;
	while (t--) {
		cout << "Case #" << ++k << ": " << run() << endl; 
	}
	return 0;
}