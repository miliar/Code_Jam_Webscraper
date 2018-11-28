#include <iostream>
#include <cstdio>
#include <set>
#include <map>

using namespace std;

int main() {
	int cases,r1,r2,curr;
	cin>>cases;
	int c = 0;
	while(cases--) {
		c++;
		set<int> v1;
		cin>>r1;
		for(int i = 0;i<4;++i) {
			for(int j = 0;j<4;++j) {
				cin>>curr;
				if(r1-1 == i) {
					v1.insert(curr);
				}
			}
		}
		cin>>r2;
		int cont = 0;
		int sol;
		for(int i = 0;i<4;++i) {
			for(int j = 0;j<4;++j) {
				cin>>curr;
				if(r2-1 == i) {
					if(v1.find(curr) != v1.end()) {
						++cont;
						sol = curr;
					}
				}
			}
		}
		if(cont == 1) {
			printf("Case #%d: %d\n",c,sol);
		}
		else if( cont == 0) {
			printf("Case #%d: Volunteer cheated!\n",c);
		}
		else {
			printf("Case #%d: Bad magician!\n",c);
		}
	}
	return 0;
}