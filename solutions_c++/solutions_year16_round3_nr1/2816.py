#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <deque>
#include <cstdio>
using namespace std;

int main() {
	freopen("A-large (4).in","r",stdin);
	freopen("c1.out","w",stdout);
	int test,t;
	cin >> t; 
	for (test=1;test<=t;test++) {
		int n;
		vector< pair<char,int> > senators;
		char c = 'A';
		cin >> n;
		int maxi1 = -100000;
		int maxi2 = -100000;
		int j;
		int index1,index2;
		int k;
		for (int i = 0; i < n; i++) {
			cin >> k;
			senators.push_back(make_pair(c,k));
			c++;
			if (k > maxi1) {
				if (k > maxi2) {
					maxi1 = maxi2;
					maxi2 = k;
					index1 = index2;
					index2 = i;
				}
				else {
					maxi1 = k;
					index1 = i;
				}
			}
		}
		//cout << maxi2 << " " << index2<< endl << maxi1 << " " << index1<<endl;
		cout << "Case #" << test << ": "; 
		while (maxi2 > maxi1) {
			senators[index2].second--;
			maxi2--;
			cout << senators[index2].first << " ";
		}
		//cout << "www" << endl;
		for (int i = 0; i < n; i++) {
			if (i != index1 && i != index2) {
				for (int j = 0; j < senators[i].second; j++) {
					cout << senators[i].first << " ";
				}
			}
		}
		//cout << "qqq" << endl;
		for (int i = 0; i < senators[index1].second; i++) {
			cout << senators[index1].first << senators[index2].first << " ";
		}
		cout << endl;

	}

	return 0;
}