
/*
  ID:wilbeib1
  PROG:magic
  LANG:C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
using namespace std;

int m1[4][4];
int m2[4][4];

int main()
{
	//freopen("magic.in","r",stdin);
	//freopen("maigic.out","w",stdout);
	int T;
	cin>>T;
	int g1, g2;
	for(int ca = 0; ca < T; ca++){
		scanf("%d", &g1);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf("%d", &m1[i][j]);

		scanf("%d", &g2);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf("%d", &m2[i][j]);

		int cnt = 0;
		int ans = 0;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				//printf("m1[g1][i]:%d, m2[g2][j]:%d\n", m1[g1][i], m2[g2][j]);
				if(m1[g1-1][i] == m2[g2-1][j]){
					ans = m1[g1-1][i];
					cnt++;
				}
			}
		if(cnt == 0)
			printf("Case #%d: Volunteer cheated!\n", ca+1);		
		else if(cnt > 1)
			printf("Case #%d: Bad magician!\n", ca+1);
		else
			printf("Case #%d: %d\n", ca+1, ans);
		
		
		

	}
	
	return 0;	  
}
