//---------------------------------------------------------------------
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

#include <vector>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <bitset>

#include <algorithm>
#include <cmath>
using namespace std;


//---------------------------------------------------------------------

int s1[4][4],s2[4][4],t,row_1,row_2;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&t);
	for (int qq=0; qq<t; qq++) {
		scanf("%d",&row_1);
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				scanf("%d",&s1[i][j]);
		scanf("%d",&row_2);
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				scanf("%d",&s2[i][j]);
		
		int cnt = 0, val = 0;
		for (int j=0; j<4; j++) {
			int x = s1[row_1-1][j];
			int Ok = 0;
			for (int q=0; q<4; q++)
				if (s2[row_2-1][q] == x) Ok = 1;
			if (Ok) {
				cnt++;
				val = x;
			}
		}

		printf("Case #%d: ",qq+1);
		if (cnt > 1) printf("Bad magician!");
		else if (cnt <= 0) printf("Volunteer cheated!");
		else printf("%d",val);
		if (qq < t-1)
			printf("\n");
	}
	

	return 0;
}