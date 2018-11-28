#include <iostream>
#include <vector>
#include <unordered_map>
#include <utility>
#include <iterator>
#include <algorithm>
using namespace std;

string eva(vector<int> v) {
	int n = v.size();
	vector<pair<int,char> > party;
	int total = 0;
	for (int i = 0; i < n; i++) {
		party.push_back(make_pair(v[i], ('A' + i)));
		total += v[i];
	}
	sort(party.begin(), party.end());
	string result = "";
	while (total > 0) {
		n = party.size();
		int i = n - 1;
		if (n >= 2 && party[i].first == party[i - 1].first && (!(n == 3 && party[i].first == 1))) {
			result = result + party[i].second + party[i - 1].second + " ";
			party[i].first--;
			party[i - 1].first--;
			total--;
			total--;
			if (party[i].first == 0) {
				party.pop_back();
				party.pop_back();
			}
		} else {
			if (party[i].first == 1) {
				result = result + party[i].second + " ";
				party[i].first --;
				total --;
				if (party[i].first == 0) {
					party.pop_back();
				}
			} else {
				result = result + party[i].second + party[i].second + " ";
				party[i].first -= 2;
				total -= 2;
				if (party[i].first == 0) {
					party.pop_back();
				}
			}
		}
		sort(party.begin(), party.end());
	}
	result = result.substr(0, result.size() - 1);
	return result;
}

int main() {
	int t;
	int n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n;  // read n and then m.
		vector<int> v;

		for (int k = 1; k <= n; k++) {
			int num;
			cin >> num;
			v.push_back(num);
		}
		
		cout << "Case #" << i << ": " << eva(v) <<endl;
		
	}
}