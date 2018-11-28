#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int>    vi;
typedef vector<ii>     vii;
const int inf = 1000000000;



int main() {
    int t;
    ios::sync_with_stdio(false);
    cin >> t;
    for(int test = 1; test <= t; test++) {
	cout << "Case #" << test << ": ";
	string s;
	int letters[26] = {0};
	vector<string> numbers = {"ZERO", "SIX", "SEVEN", "EIGHT", "FIVE", "NINE", "TWO", "ONE", "THREE", "FOUR"};
	char uniq[] = {'Z', 'X', 'S', 'G', 'V', 'I', 'W', 'N', 'H', 'R'};
	char mean[] = {'0','6','7','8','5','9','2','1','3','4'};
	int res[10] = {0};
	cin >> s;
	
	for(auto& c : s)
	    letters[c - 'A']++;
	
	int app;
	for(int i = 0; i<10; i++) {
	app = letters[uniq[i] - 'A'];
	res[mean[i] - '0'] = app;
	for(auto c : numbers[i])
	    letters[c - 'A'] -= app;
	}
	
	for(int i = 0; i < 10; i++)
	    for(int j = 0; j < res[i]; j++)
		cout << (char)('0' + i);

	cout << endl;
    }
    return 0;
}
