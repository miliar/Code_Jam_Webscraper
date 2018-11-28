#include <iostream>
#include <stdio.h>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <sstream>
#include <cmath>
#define ull unsigned long long int
#define ll long long
#define Max(a,b) a >b ? a :b
#define S(n) scanf("%d",&n)
#define Sl(n) scanf("%ld",&n)
#define Sll(n) scanf("%lld",&n)
#define li long int
using namespace std;
int main()
{
	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	int k;
	for(k = 1; k <= t; k++) {
		int n1;
		int n2;
		int a[10][10];
		int b[10][10];
		cin >> n1;
		int i,j;
		for(i = 1; i <= 4; i++) {
			for(j = 1; j <= 4; j++) {
				cin >> a[i][j];
			}
		}
		cin >> n2;
		for(i = 1; i <= 4; i++) {
			for(j = 1; j <= 4; j++) {
				cin >> b[i][j];
			}
		}
		int c4 = 0;
		int c1,c2,c3;
		c1 = c2 =c3 = 0;
		for(i = 1; i <= 4; i++) {
			if(a[n1][1] == b[n2][i]) {
				c1 = 1;
				break;
			}
		}
		for(i = 1; i <= 4; i++) {
			if(a[n1][2] == b[n2][i]) {
				c2 = 1;
				break;
			}
		}
		for(i = 1; i <= 4; i++) {
			if(a[n1][3] == b[n2][i]) {
				c3 = 1;
				break;
			}
		}
		for(i = 1; i <= 4; i++) {
			if(a[n1][4] == b[n2][i]) {
				c4 = 1;
				break;
			}
		}
		cout << "Case #" << k << ": "; 
		if(c1 == 1 && c2 == 1 && c3== 1 && c4 == 1) {
			cout << "Bad magician!\n";
		} else if(c1 == 0 && c2 == 0 && c3 == 0 && c4 ==0) {
			cout << "Volunteer cheated!\n";
		} else {
			if(c1 == 1 && c2 ==0 && c3 == 0 && c4 == 0) {
				cout << a[n1][1] << endl;
			} else if(c1 == 0 && c2 ==1 && c3 == 0 && c4 == 0) {
				cout << a[n1][2] << endl;
			} else if(c1 == 0 && c2 ==0 && c3 == 1 && c4 == 0) {
				cout << a[n1][3] << endl;
			} else if(c1 == 0 && c2 ==0 && c3 == 0 && c4 == 1) {
				cout << a[n1][4] << endl;
			} else {
				cout << "Bad magician!\n";
			}
		}
	}
	

	return 0;
}
