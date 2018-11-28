#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int calc(vector<int> s, int x) {
	int ans = 0;
	for (int i=0; i<s.size(); i++) {
		if (s[i]>x) {
			ans+= (s[i]/x) - (s[i]%x==0);
		}
	}
	return ans+x;
}

int main() {
	int t;
	cin>> t;
	for(int tn=0; tn<t; tn++) {
		int d;
		cin>>d;
		int maxp = 0;
		vector<int> pancakes;
		for(int i=0; i<d; i++) {
			int tmp;
			cin>>tmp;
			if (maxp<tmp) {
				maxp = tmp;
			}
			pancakes.push_back(tmp);
		}
		sort(pancakes.begin(), pancakes.end());
		int ans = maxp;
		for (int i=1; i<=maxp; i++) {
			int tmp = calc(pancakes, i);
			if (ans>tmp) {
				ans = tmp;
			}
		}
		cout << "Case #"<<tn+1<<": "<<ans<<endl;
	}
}