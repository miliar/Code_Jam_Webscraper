#include <iostream> 
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <functional>
#include <cstring>
#include <algorithm>
#include <map>
#include <cmath>
#include <ctime>
#include <unordered_map>

using namespace std;

int solve() {
	string s;
	cin >> s;
	s += '+';
	int cnt = 0;
	for (int i = 0; i < s.size() - 1; ++i) {
		if (s[i] != s[i + 1]) ++cnt;
	}
	return cnt;
}

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	}

}