#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int T, r1, r2;
int con[17];


int main(){

	scanf("%d ", &T);

	for(int cas=1;cas<=T;cas++){
		scanf("%d ", &r1);

		for(int i=1;i<=16;i++) con[i] = 0;

		for(int i=1; i<=4;i++){
			for(int j=1;j<=4;j++){
				int a;
				scanf("%d ", &a);
				if(i == r1) con[a] = 1;
			}
		}	

		scanf("%d ", &r2);

		for(int i=1; i<=4;i++){
			for(int j=1;j<=4;j++){
				int a;
				scanf("%d ", &a);
				if(i == r2) con[a] += 1;
			}
		}


		int ct = 0, pos = 0;

		for(int i=1;i<=16;i++) if(con[i] == 2){ ct++; pos = i;}

		if(ct == 0)
			printf("Case #%d: Volunteer cheated!\n", cas);
		else if(ct == 1)
			printf("Case #%d: %d\n", cas, pos);
		else
			printf("Case #%d: Bad magician!\n", cas);		

	}

	return 0;
}
