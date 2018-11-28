#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
using namespace std;
int main () {
	freopen ("C:\\Users\\shreshtha24\\Desktop\\ans.txt", "w", stdout);
	int t, a1, a2, itt, itr2;
	int ptr = 1, res = 0, p = 0;
	int aaa[4][4], bbb[4][4];
	cin >> t;
	while ( t --) {
		res = 0;
		p = 0;
		t = t+1;
		t = t-1;
		aaa[4][4];
		bbb[4][4];
		cin >> a1 ;
		for ( itt = 0; itt < 4; itt ++) {
			for ( itr2 = 0; itr2 < 4; itr2 ++) {
				cin >> aaa[itt][itr2];
			}
		}
		cin >> a2;
		for ( itt = 0; itt < 4; itt ++) {
			for ( itr2 = 0; itr2 < 4; itr2 ++) {
				cin >> bbb[itt][itr2];
			}
		}
		res = 0;
		p = 0;
		for ( itt = 0; itt < 4; itt ++) {
			for ( itr2 = 0; itr2 < 4; itr2 ++) {
				if ( aaa[a1-1][itt] == bbb[a2-1][itr2] ) {
					res = res + 1;
					p = aaa[a1-1][itt];
				}
			}
		}
		if ( res == 1 )
			cout << "Case #" << ptr << ": " << p << endl;
		else if ( res == 0) 
			cout << "Case #" << ptr << ": Volunteer cheated!" << endl;
		else if ( res > 1 )
			cout << "Case #" << ptr << ": Bad magician!" << endl;
		
		ptr ++;
	}
	return 0;
}