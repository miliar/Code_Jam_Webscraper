#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <stack>

using namespace std;



int n;
int tot;
int a[50];

void parse() {
 	cin >> n;
 	tot = 0;
 	for (int i = 0; i < n; i++){
 		cin >> a[i];
 		tot += a[i];
 	}
}

bool check(){
	for (int i = 0; i < n; i++)
		if (a[i]*2 > tot)
			return false;
	return true;
}
void solve() {
	while (tot){
	int maxp = -1;
	for (int i = 0; i < n; i++)
		if (maxp == -1 || a[i] > a[maxp])
			maxp = i;

	a[maxp] -= 2;
	tot -= 2;
	if (check())
		cout << " " << char(maxp+ 'A') << char(maxp +'A');
	else {
		a[maxp] += 1;
		tot += 1;
		cout << " " << char(maxp+ 'A');
		if (!check()){
			tot -= 1;
			for (int i = 0; i < n; i++)
				if (a[i] > 0 && i != maxp){
					a[i] --;
					if (check()){
						cout << char (i + 'A');
						break;
					}
					a[i]++;
				}
		}
	}
}
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++){
		parse();
		cout << "Case #" << i << ":";
		solve();
		cout << endl;
	}
	return 0;
}



