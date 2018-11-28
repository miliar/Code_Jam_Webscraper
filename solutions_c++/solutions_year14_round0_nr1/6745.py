#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;
int main()
{
	int t,n1,n2,c,d;
	scanf("%d",&t);
	for (int q = 1; q <= t; q++) {
		set <int> s1;
		c = 0;
		int a[4][4],b[4][4];
		scanf("%d",&n1);
		n1--;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&n2);
		n2--;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d",&b[i][j]);
			}
		}
		for (int j = 0; j < 4; j++) {
			s1.insert(a[n1][j]);
		}
		for (int j = 0; j < 4; j++) {
			if (s1.count(b[n2][j])) {
				c++;
				d = b[n2][j];
			}
		}
		if (c == 1) {
			printf("Case #%d: %d\n",q,d);
		} else if (c > 1){
			printf("Case #%d: Bad magician!\n",q);
		} else if (c == 0) {
			printf("Case #%d: Volunteer cheated!\n",q);
		}
	}
}
