#include <cstdio>
#include <iostream>
using namespace std;

#define S(n)	scanf("%d",&n)

int main(){
	//freopen("in.in" , "r" , stdin);
    //freopen("out.out" , "w" , stdout);

	int c1[5][5] , c2[5][5];
	int x1 , x2 , TC , cc = 0 , cnt , ans;

	S(TC);
	while(TC--){
		cnt = 0;

		S(x1);
		x1--;
		for(int i=0; i<4; i++)for(int j = 0; j < 4; j++)	S(c1[i][j]);
		S(x2);
		x2--;
		for(int i=0; i<4; i++)for(int j = 0; j < 4; j++)	S(c2[i][j]);
		
		for(int i=0; i<4; i++)
			for(int j = 0; j < 4; j++){
				if(c1[x1][i] == c2[x2][j]){
					cnt++;
					ans = c1[x1][i];
				}
		}
		
		if(cnt == 1)
			printf("Case #%d: %d\n" , ++cc , ans);
		else if(cnt == 0)
			printf("Case #%d: Volunteer cheated!\n" , ++cc);
		else
			printf("Case #%d: Bad magician!\n" , ++cc);
	}


	return 0;
}