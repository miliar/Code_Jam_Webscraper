/// In the name of God

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>

using namespace std;


int a[32];
int main(){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T, t, n, i, j, k, r, s;
	cin >> T;
	for (t = 1; t <= T; t++){
		for (i = 0; i < 32; i++)a[i] = 0;
		for (s = 1; s < 3; s++){
			cin >> n;
			for (i = 1; i < 5; i++){
				for (j = 1; j < 5; j++){
					cin >> k;
					if (i == n)
						a[k]++;
				}
			}
		}
		
		k = 0;
		r = 0;
		for (i = 1; i < 17; i++)
		if (a[i] == 2){ r++; k = i; }
		cout << "Case #" << t << ": ";
		if (r == 1)
			cout << k << endl;
		else if (r != 0)
			cout << "Bad magician!" << endl;
		else
			cout<<"Volunteer cheated!" << endl;
	}
	return 0;
}
