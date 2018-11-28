/*
 * magician.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: saha
 */
#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T,a,b,p,t;
	vector<int> f,s;
	cin >> T;
	p=1;
	while(T--) {
		cin >> a;
		f.clear();
		s.clear();
		bool isMag = false;
		bool isCheat = false;
		for(int i=0;i<4;i++) {
			if(i+1 != a) {
				cin >> t >> t >> t >> t;
			}
			else {
				for(int j=0; j<4; j++) {
					cin >> t;
					f.push_back(t);
				}
			}
		}

		cin >> b;

		for(int i=0;i<4;i++) {
			if(i+1 != b) {
				cin >> t >> t>> t >> t;
			}
			else {
				for(int j=0; j<4; j++) {
					cin >> t;
					s.push_back(t);
				}
			}
		}
		bool isFound = false;
		int res=-1;
//		cout << f.size() << " " << s.size() << endl;
		for(int i=0; i<4; i++) {
			for(int j=0; j<4 ; j++) {
				if(f[i] == s[j]) {
					if(!isFound) {
						isFound = true;
						res = f[i];
					} else {
						isMag = true;
					}
				}
			}
		}
		if(!isFound)
			cout << "Case #" << p << ": Volunteer cheated!" << endl;
		else if(isMag)
			cout << "Case #" << p << ": Bad magician!" << endl;
		else
			cout << "Case #" << p << ": " << res << endl;
		p++;
	}
}



