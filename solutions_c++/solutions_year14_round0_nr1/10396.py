// GCJ-A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;



void solveA()
{
	int T;
	int casetest = 1;
	scanf("%d",&T);
	while(T--){
		int i,j;
		int ans_a, ans_b;
		int matrixA[4][4]={0};
		int matrixB[4][4]={0};
		
		scanf("%d",&ans_a);
		for (i = 0; i < 4; i++){
			for (j = 0; j < 4; j++){
				scanf("%d",&matrixA[i][j]);
			}
		}
		
		scanf("%d",&ans_b);
		for (i = 0; i < 4; i++){
			for (j = 0; j < 4; j++){
				scanf("%d",&matrixB[i][j]);
			}
		}

		int mask[17]={0};
		int found = 0;
		int ans = 0;
		for (i = 0; i < 4; i++){
			mask[matrixA[ans_a - 1][i]] = 1;
			//cout<<matrixA[ans_a - 1][i]<<" ";
		}

		for (i = 0; i < 4; i++){
			//cout<<matrixB[ans_b - 1][i]<<" ";
			if (mask[matrixB[ans_b - 1][i]] != 0)
			{
				//cout<<"+";
				found++;
				ans = matrixB[ans_b - 1][i];
			}
		}
		printf("Case #%d: ", casetest);
		if (found == 0){
			printf("Volunteer cheated!\n");
		}else if (found == 1){
			printf("%d\n", ans);
		}else
		{
			printf("Bad magician!\n");
		}
		casetest++;
	}

}

int _tmain(int argc, _TCHAR* argv[])
{

	freopen("d:\\A-small-attempt0.in", "r", stdin);
	freopen("d:\\A-small-attempt0.out", "w", stdout);

	solveA();

	return 0;
}

