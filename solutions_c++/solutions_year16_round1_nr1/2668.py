#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int>    vi;
typedef vector<ii>     vii;
const int inf = 1000000000;

int main() {
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int a = 1; a <= t; a++) {
	cout << "Case #" << a << ": ";
	deque<char> res;
	string input;
	cin >> input;
	for(auto& c : input) {
	    if(res.empty() || c >= res.front()) res.push_front(c);
	    else res.push_back(c);
	}
	for(auto& c : res) {
	    cout << c;
	}
	cout << endl;
    }
    

    return 0;
}
