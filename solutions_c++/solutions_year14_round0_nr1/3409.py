#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
using namespace std;
int main () {
	freopen ("C:\\Users\\shreshtha24\\Desktop\\ans2.txt", "w", stdout);
	int test, a11, a22, iii, jjj;
	int ptr = 1, ress = 0, p = 0;
	int array1[4][4], array2[4][4];
	scanf ("%d", &test);
	while ( test --) {
		ress = 0;
		p = 0;
		test = test+1;
		test = test-1;
		cin >> a11 ;
		for ( iii = 0; iii < 4; iii ++) {
			for ( jjj = 0; jjj < 4; jjj ++) {
				scanf ("%d", &array1[iii][jjj]);
			}
		}
		cin >> a22;
		for ( iii = 0; iii < 4; iii ++) {
			for ( jjj = 0; jjj < 4; jjj ++) {
				scanf ("%d", &array2[iii][jjj]);
			}
		}
		ress = 0;
		p = 0;
		int a = 1;
		for ( iii = 0; iii < 4; iii ++) {
			for ( jjj = 0; jjj < 4; jjj ++) {
				if ( array1[a11-1][iii] == array2[a22-1][jjj] ) {
					ress = ress + a;
					p = array1[a11-1][iii];
				}
			}
		}
		if ( ress == 0) 
			cout << "Case #" << ptr << ": Volunteer cheated!" << endl;
		else if ( ress == 1 )
			cout << "Case #" << ptr << ": " << p << endl;
		else if ( ress > 1 )
			cout << "Case #" << ptr << ": Bad magician!" << endl;
		
		ptr ++;
	}
	return 0;
}