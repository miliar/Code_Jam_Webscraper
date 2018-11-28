#include<stdio.h>
#include<iostream>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#define print(Z,a,b) for (int __z = a; __z < b; __z ++) cout << Z[__z] << " ";
#define scan(Z,a,b) for (int __z = a; __z < b; __z ++) cin >> Z[__z];
#define bit(_z) (1ll << _z)
using namespace std;

int t;
int n;
bool possible[100];

int main () {
	cin >> t;
	
	int caze = 0;
	while (t --) {
		++ caze;
		
		memset(possible, 1, sizeof (possible));
		for (int z = 0; z < 2; z ++) {
			int r;
			cin >> r;
			for (int i = 0; i < 4; i ++) {
				for (int j = 0; j < 4; j ++) {
					int num;
					cin >> num;
					if (i + 1 != r)
						possible[num] = 0;
				}
			}
		}
	
		int ak = 0, last;
		for (int i = 1; i <= 16; i ++) {
			ak += possible[i];
			if (possible[i])
				last = i;
		}
		
		cout << "Case #" << caze << ": ";
		
		if (ak == 0)
			cout << "Volunteer cheated!" << endl;
		else if (ak > 1)
			cout << "Bad magician!" << endl;
		else
			cout << last << endl;
		
	}
	
	return 0;
}  	
