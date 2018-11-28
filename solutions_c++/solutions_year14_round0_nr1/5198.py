//============================================================================
// Name        : Magic.cpp
// Author      : alpc92
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <set>
using namespace std;

int main(void) {
	freopen("out","w",stdout);
	int mat[2][4][4], ans[2];
	int T;
	set<int> st[2];
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		st[0].clear();
		st[1].clear();
		for (int i = 0; i < 2; ++i) {
			cin >> ans[i];
			--ans[i];
			for (int j = 0; j < 4; ++j)
				for (int k = 0; k < 4; ++k) {
					cin >> mat[i][j][k];
					if (i==0&&j==ans[i])st[0].insert(mat[i][j][k]);
					else if (i==1&&ans[i]==j&&st[0].find(mat[i][j][k])!=st[0].end())st[1].insert(mat[i][j][k]);

				}
		}
		switch (st[1].size()){
		case 0:{
			puts("Volunteer cheated!");
			break;
		}
		case 1:{
			cout<<*st[1].begin()<<endl;
			break;
		}
		default:{
			puts("Bad magician!");
			break;
		}
		}
	}
	return 0;
}
