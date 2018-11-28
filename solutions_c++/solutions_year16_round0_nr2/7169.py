#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++) {
		string sides;
		int plusend = 0, minusend = -1, count = 0;
		cin >> sides;
		while(true) {
			int j;
			for(j = plusend; j < sides.length(); j++) {
				if(sides[j] == '+') {
					if(minusend == -1) continue;
					break;
				}
				if(sides[j] == '-') {
					if(minusend == -1) plusend = j-1;
					minusend = j;
				}
			}
			if(j == sides.length() && minusend == -1) break;
			if(plusend == -1) count++;
			else count += 2;
			plusend = minusend+1;
			minusend = -1;
		}
		printf("Case #%d: %d\n", i+1, count);
	}
}