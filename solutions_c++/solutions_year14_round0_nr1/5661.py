#include<cstdio>
#include<cstring>
#include<fstream>
#include<iostream>
using namespace std;
const int N = 4;
int mp1[N+1][N+1], mp2[N+1][N+1];
int main()
{
	int t;
	scanf("%d",&t);
	for (int T = 1; T <= t; T++) {
		int row1, row2;
		scanf("%d",&row1);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				scanf("%d",&mp1[i][j]);
		scanf("%d",&row2);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				scanf("%d",&mp2[i][j]);
		cout << row1 << " "  << row2 << endl;
		int ans = 0, ret;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				if (mp1[row1][i] == mp2[row2][j]) {
					ans++;
					ret = mp1[row1][i];
				}
		
		if (ans == 1) 
			printf("Case #%d: %d\n",T,ret);
		else if (ans > 1) 
			printf("Case #%d: Bad magician!\n",T);
		else if (ans == 0)
			printf("Case #%d: Volunteer cheated!\n", T);
	}
}