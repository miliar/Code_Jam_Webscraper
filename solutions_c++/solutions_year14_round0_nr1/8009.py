#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <vector>
using namespace std;
int main() {
	int _, x, y, tmp, ca(0); cin>>_;
	while(_--) {
		vector<int> a, b, res;
		cin>>x;
		for(int i(0); i!=4; ++i) {
			for(int j(0); j!=4; ++j) {
				cin>>tmp;
				if(i+1==x) {
					a.push_back(tmp);
				}
			}
		}
		cin>>y;
		for(int i(0); i!=4; ++i) {
			for(int j(0); j!=4; ++j) {
				cin>>tmp;
				if(i+1==y) {
					b.push_back(tmp);
				}
			}
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		set_intersection(a.begin(), a.end(), b.begin(), b.end(), back_inserter(res));
		printf("Case #%d: ", ++ca);
		switch(res.size()) {
			case 0:
				puts("Volunteer cheated!");
				break;
			case 1:
				cout<<res.front()<<'\n';
				break;
			default:
				puts("Bad magician!");
		}
	}
	return 0;
}
