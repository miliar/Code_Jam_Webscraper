#include <stdio.h>

using namespace std;


int lawn[100][100];

bool check(int h, int w){
	for (int i = 0; i < h; i++){
		for (int j = 0; j < w; j++){
			short checker = 0;
			//printf("%d %d\n", i, j);
			for (int k = 0; k < h; k++){
				if (lawn[i][j] < lawn[k][j]){
					//printf("%d %dxxxxxx\n", lawn[i][j], lawn[k][j]);
					for (int k = 0; k < w; k++){
						if (lawn[i][j] < lawn[i][k]){
							return false;
						}
					}
				}
			}
		}
	}
	return true;
}

int main(){
	
	int instances;
	int h, w;
	scanf("%d", &instances);
	for (int i = 0; i < instances; i++){
		scanf("%d", &h);
		scanf("%d", &w);
		for (int j = 0; j < h; j++){
			for (int k = 0; k < w; k++){
				scanf("%d", &(lawn[j][k]));
				//printf("%d", lawn[j][k]);
			}
			//printf("\n");
		}
		printf("Case #%d: %s\n", i+1, (check(h, w)?"YES":"NO"));
	}
	return 0;
}
