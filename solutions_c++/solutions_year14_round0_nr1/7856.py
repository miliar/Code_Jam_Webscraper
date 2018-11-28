#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("a_input.txt", "r", stdin);
	freopen("a_output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		int x, y, mx[4][4], my[4][4];
		
		scanf("%d", &x);
		for(int i=0; i<4; i++) for(int j=0; j<4; j++) scanf("%d", &mx[i][j]);
		scanf("%d", &y);
		for(int i=0; i<4; i++) for(int j=0; j<4; j++) scanf("%d", &my[i][j]);
		
		x--;
		y--;
		
		int c = 0, r = -1;
		for(int i=0; i<4; i++) for(int j=0; j<4; j++){
			if( mx[x][i] == my[y][j] ){
				c++;
				r = mx[x][i];
			}
		}
		
		printf("Case #%d: ", t);
		
		if(c == 0) printf("Volunteer cheated!");
		else if(c == 1) printf("%d", r);
		else printf("Bad magician!");
		
		printf("\n");
	}
	return 0;
}
