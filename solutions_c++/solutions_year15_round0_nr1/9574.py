#include <bits/stdc++.h>
using namespace std;
int main() {
	int T, n, personas, total;
	string s;
	cin>>T;
	for(int caso=1 ; caso<=T ; caso++)  {
		cin>>n>>s;
		n++;
		personas = total = 0;
		for(int i=0 ; i<n ; i++) {
			int val = (s[i] - '0');
			total += val;
			if(personas < i) {
				personas = i;
			}
			personas += val;
		}
		printf("Case #%d: %d\n", caso, personas - total);
	}
	return 0;
}