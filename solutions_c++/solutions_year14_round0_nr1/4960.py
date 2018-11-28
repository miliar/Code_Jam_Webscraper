#include <iostream>
#include <algorithm>
#define MAXN 1000
#include <cstdio>
using namespace std; 
int a[MAXN][MAXN];
int b[MAXN][MAXN];
int main(void){
	FILE *fp;
	fp = fopen("out.txt", "w");
	int T;
	cin >> T;
	for(int t=1; t<=T; ++t){
		int x, y;
		cin >> x;
		for(int i=1; i<=4; ++i){
			for(int j=1; j<=4; ++j){
				cin >> a[i][j];
			}
		}
		cin >> y;
		for(int i=1; i<=4; ++i){
			for(int j=1; j<=4; ++j){
				cin >> b[i][j];
			}
		}
		int flag = 0;
		int card;
		for(int i=1; i<=4; ++i){
			for(int j=1; j<=4; ++j){
				if(a[x][i] == b[y][j]){
					flag++;
					card = a[x][i];
				}
			}
		}
		if(flag == 1){
			fprintf(fp, "Case #%d: %d\n", t, card);
		}
		else if(flag > 1){
			fprintf(fp, "Case #%d: Bad magician!\n", t);
		} else {
			fprintf(fp, "Case #%d: Volunteer cheated!\n", t);
		}
	}
	return 0;
}
