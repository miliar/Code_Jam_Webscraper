#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int max_time(int pancakes, int splits){
	if (splits == 0) return pancakes;
	switch (pancakes) {
		case 1: return 10; 
		case 2: return 10; 
		case 3: return 10;
		case 4: if (splits == 1) return 2; else return 10;
 		case 5: if (splits == 1) return 3; else return 10;
		case 6: if (splits == 1) return 3; else return 10;
		case 7: if (splits == 1) return 4; else return 10;
		case 8: if (splits == 1) return 4; else return 10;
		case 9: if (splits == 1) return 5; else if (splits == 2) return 3; else return 10;
		case 10: return 0;
	}
}

int find_max(int M[6], int D){
	int max = 0;
	for (int i = 0; i < D; i++)
		if (M[i]>max) max = M[i];
	return max;
}

int main()
{
	int T;
	scanf("%d", &T);
	int D;
	int array[3][3][3][3][3][3];
	
	for (int i = 1; i <= T ; i ++){
	
		scanf("%d", &D);
		int P[D];

		for (int j=0; j<D; j++)
			scanf("%d", &P[j]);
		for (int j = D; j<6; j++)
			P[j]=10;
		sort(P, P+D);
		
		int M[6];
		
		int result[12];
		for (int j = 0; j < 12; j++) 
			result[j] = 10;
		
		int res = 10;
		for (int j = 0; j < 3; j++)
			for (int k = 0; k < 3; k++)
				for (int l = 0; l < 3; l++)
					for (int m = 0; m < 3; m++)
						for (int n = 0; n < 3; n++)
							for (int q = 0; q < 3; q++){
								M[0] = max_time(P[0], j);
								M[1] = max_time(P[1], k);
								M[2] = max_time(P[2], l);
								M[3] = max_time(P[3], m);
								M[4] = max_time(P[4], n);
								M[5] = max_time(P[5], q);
								int time = find_max(M, D)+j+k+l+m+n+q;
								if (time < res) res = time;
							}

		printf("Case #%d: %d\n", i, res);
	}
	
}
