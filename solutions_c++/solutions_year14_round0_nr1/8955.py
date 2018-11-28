/*
 * A.cpp
 *
 *  Created on: Apr 13, 2014
 *      Author: Yasser
 */

#include<iostream>
using namespace std;
int a[4][4], b[4][4];
int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T,x,y;
	scanf("%d", &T);

	for (int tt = 0; tt < T; tt++) {
		scanf("%d", &x);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &a[i][j]);

		scanf("%d", &y);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &b[i][j]);

		int found = 0, ans = -1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(a[x-1][i] == b[y-1][j])
					ans=a[x-1][i], found++;
		if(found == 1)
			printf("Case #%d: %d\n",tt+1, ans);
		else if(found == 0)
			printf("Case #%d: Volunteer cheated!\n",tt+1);
		else
			printf("Case #%d: Bad magician!\n",tt+1);
	}

	return 0;
}
