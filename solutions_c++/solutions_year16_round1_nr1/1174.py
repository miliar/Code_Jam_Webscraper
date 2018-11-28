#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <cmath>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
using namespace std;

typedef long long ll;

string s;
vector<char> output;

int main() {

	ll n;
	cin >> n;
	for(ll i = 0; i < n; i++) {
		output.clear();
		cin >> s;
		ll len = s.length();
		for(ll j = 0; j < len; j++) {
			if(j == 0 || (int)s[j] < (int)output[0])
				output.pb(s[j]);
			else
				output.insert(output.begin(), s[j]);			
		}
		cout << "Case #" << i + 1 << ": ";
		for(ll j = 0; j < len; j++)
			cout << output[j];
		cout << endl;
	}
	return 0;
}
