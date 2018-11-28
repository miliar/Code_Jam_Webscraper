#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int t,j;
	cin >> t;
	for (j = 0; j < t; j++) {
		int n,g,l,i;
		char a[100005];
		cin >> n;
		g = 0;
		l = 0;
		scanf("%s", a);
		for (i = 0; i < n; i++) {
			g = g + a[i]-'0';
			if (g < i+1) {
				l = max(l,i-g+1);
			}
		}
		cout <<"Case #"<<j+1<<": "<< l << endl;
	}
	return 0;
}
