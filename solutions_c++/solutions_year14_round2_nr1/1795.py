#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

#define abs(x) (((x) > 0)? (x) : (-(x)))

//#define DEBUG

int main()
{
	int t;
	cin >> t;
	for (int j = 1; j <= t; j++) {
		int n;
		cin >> n;
		string S1, S2;
		cin >> S1 >> S2;
		vector<pair<char, int> > multiset1;
		vector<pair<char, int> > multiset2;
		multiset1.push_back(make_pair(S1[0], 1));
		int x = 0;
		for (int i = 1; i < S1.size(); i++) {
			if (multiset1[x].first == S1[i]) {
				multiset1[x].second++;
			} else {
				x++;
				multiset1.push_back(make_pair(S1[i], 1));
			}
		}
		multiset2.push_back(make_pair(S2[0], 1));
		x = 0;
		for (int i = 1; i < S2.size(); i++) {
			if (multiset2[x].first == S2[i]) {
				multiset2[x].second++;
			} else {
				x++;
				multiset2.push_back(make_pair(S2[i], 1));
			}
		}

#ifdef DEBUG
	for (int i = 0; i < multiset1.size(); i++) {
		cout << multiset1[i].first << " " << multiset1[i].second << endl;
	}
	cout << endl;
	for (int i = 0; i < multiset2.size(); i++) {
		cout << multiset2[i].first << " " << multiset2[i].second << endl;
	}
	cout << endl;
#endif

		bool flag = 1;
		int cost = 0;
		if (multiset1.size() != multiset2.size()) {
			flag = 0;
		} else {
			for (int i = 0; i < multiset1.size(); i++) {
				if (multiset1[i].first != multiset2[i].first) {
					flag = 0;
					break;
				} else {
					cost += abs(multiset1[i].second - multiset2[i].second);	
				}
			}
		}

		cout << "Case #" << j << ": " ;
		if (flag)
			cout << cost << endl;
		else 
			cout << "Fegla Won" << endl;
	}
}
