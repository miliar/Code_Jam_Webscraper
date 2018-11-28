#include <stdio.h>
#include <string.h>
using namespace std;
int board[5][5];
bool ans[20];
int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t, ri, a1, a2;
	scanf("%d", &t);
	for(int ind=1; ind<=t; ind++){	
		printf("Case #%d: ", ind);
		scanf("%d", &a1);
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				scanf("%d", &board[i][j]);
			}
		}
		memset(ans, false, sizeof(ans));
		for(int i=0; i<4; i++)
			ans[board[a1-1][i]]=true;
		scanf("%d", &a2);
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				scanf("%d", &board[i][j]);
			}
		}
		int cont=0, answer;
		for(int i=0; i<4; i++){
			if(ans[board[a2-1][i]]){
				answer=board[a2-1][i];
				cont++;
			}
		}
		if(cont>1) printf("Bad magician!\n");
		else if(cont==0) printf("Volunteer cheated!\n");
		else printf("%d\n", answer);
	}
	return 0;
}