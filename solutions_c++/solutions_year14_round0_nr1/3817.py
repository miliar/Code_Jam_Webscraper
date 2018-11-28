#include <stdio.h>
#include <cstring>
using namespace std;

int main(){
	freopen("A-small-attempt5.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n, c, index1, index2, count, res, a[4][4], b[4][4];
	scanf("%d", &n);
	for(int k=1; k<=n; k++){
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		scanf("%d", &index1);
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				scanf("%d", &a[i][j]);		
			}
		}
		scanf("%d", &index2);
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				scanf("%d", &b[i][j]);		
			}
		}
		index1 = index1 - 1;
		index2 = index2 - 1;
		count = 0;
		res = 0;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(a[index1][i] == b[index2][j]){
					count++;
					res = a[index1][i];
				} 
			}
		}
		if(count == 1) printf("Case #%d: %d", k, res);
		else if(count == 0) printf("Case #%d: Volunteer cheated!", k);
		else printf("Case #%d: Bad magician!", k);	
		if(k != n){
			printf("\n");
		}
	}
	return 0;
} 
