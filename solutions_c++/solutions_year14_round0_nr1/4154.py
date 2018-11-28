#include <iostream>
#include <stdio.h>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <math.h>
#include <map>

using namespace std;

int main(int argc, char** argv) {
	int T;
	cin >> T;

	vector<int> t1(4,0);
	vector< vector<int> > temp1(4,t1);
	vector< vector<int> > temp2 = temp1;

	int x, ans1, ans2;

	for(int i=0; i<T; i++) {
		cin >> ans1;
		for(int j=0; j<4; j++) {
			for(int k=0; k<4; k++) {
				cin >> x;
				temp1[j][k] = x;
			}
		}
		cin >> ans2;
		for(int j=0; j<4; j++) {
			for(int k=0; k<4; k++) {
				cin >> x;
				temp2[j][k] = x;
			}
		}
		int ans = 0;
		int finalans;
		map<int,int> m;
		for(int j=0; j<4; j++) {
			m[temp1[ans1-1][j]]++;
			m[temp2[ans2-1][j]]++;
		}
		for(map<int,int>::iterator it=m.begin(); it!=m.end(); it++) {
			if(it->second == 2 && ans == 0) { 
				ans = 1; finalans = it->first;
			} else if(it->second == 2 && ans == 1) {
				ans = 2;
			}
		}
		if(ans == 0)
			cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
		else if(ans == 1)
			cout << "Case #" << i+1 << ": " << finalans << endl;
		else
			cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
	}
}
