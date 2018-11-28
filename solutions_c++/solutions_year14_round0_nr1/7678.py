#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <iostream>
using namespace std;
bool ha[100];
int tmp[100];
void work() {
	int r1,r2,cnt=0,ans;
	memset(ha, 0, sizeof(ha));
	scanf("%d",&r1);
	for (int i=0 ; i<4 ; i++ ) {
		for (int j=0 ; j<4 ; j++ ) scanf("%d",&tmp[j]);
		if (i+1==r1) {
			for (int j=0 ; j<4 ; j++ ) ha[tmp[j]] = true;
		}
	}
	scanf("%d",&r2);
	for (int i=0 ; i<4 ; i++ ) {
		for (int j=0 ; j<4 ; j++ ) scanf("%d",&tmp[j]);
		if (i+1==r2) {
			for (int j=0 ; j<4 ; j++ ) if (ha[tmp[j]]) {
				cnt ++;
				ans = tmp[j];
			}
		}
	}
	if (cnt==0) printf("Volunteer cheated!\n");
	else if (cnt==1) printf("%d\n",ans);
	else printf("Bad magician!\n");
}

int main() {
	freopen("test.txt", "r", stdin);
	freopen("ans.txt", "w", stdout);
	int cas;
	scanf("%d",&cas);
	for (int t=1 ; t<=cas ; t++ ) {
		printf("Case #%d: ",t);
		work();
	}
	return 0;
}