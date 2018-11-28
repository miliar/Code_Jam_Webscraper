#include <cstdio>
#include <iostream>
using namespace std;

int main() {
	int tc; scanf("%d",&tc);
	for(int d = 1; d<=tc ; d++) {
		int smax; scanf("%d", &smax);
		string temp; cin >> temp;
		int countStanding = 0;
		int friendsNeeded = 0;
		for(int i=0;i<=smax;i++){
			int curr = temp[i] - '0';
			if (curr > 0) {
				if(countStanding >= i) {
					countStanding += curr;
				}
				else {
					friendsNeeded += (i-countStanding);
					countStanding += (i-countStanding)+curr;
				}
			}
		}
		printf("Case #%d: %d\n",d,friendsNeeded);
	}
	return 0;
}