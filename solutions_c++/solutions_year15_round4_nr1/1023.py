#include<stdio.h>
#include<vector>
#include<cmath>
#include<memory.h>
#include<algorithm>
using namespace std;
int N,R,C;
char input[110][110]= {0,};

bool isit(int i, int j){
	for(int k = 0; k < i; k++)
		if(input[k][j] != '.') return true;
	for(int k = i+1; k < R; k++)
		if(input[k][j] != '.') return true;
	for(int k = 0; k < j; k++)
		if(input[i][k] != '.') return true;
	for(int k = j+1; k < C; k++)
		if(input[i][k] != '.') return true;
	return false;	
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-output.txt","w",stdout);
	int T;
	scanf("%d", &T);
	for(int tc = 1; tc <= T; tc++){
		printf("Case #%d: ", tc);
		memset(input,0,sizeof(input));
		int ans=0, flag;
		scanf("%d%d", &R,&C);
		for(int i = 0; i < R; i++)
			scanf("%s", input[i]);
		for(int i = 0; i < R; i++){
			for(int j = 0; j < C; j++){
				int k;
				flag=0;
				if(input[i][j] == '^'){
					for(k = i-1; k >= 0; k--){
						if(input[k][j] != '.') break;
					}
					if(k == -1) flag=1;
				}
				if(input[i][j] == '>'){
					for(k = j+1; k < C; k++){
						if(input[i][k] != '.') break;
					}
					if(k == C) flag=1;
				}
				if(input[i][j] == '<'){
					for(k = j-1; k >= 0; k--){
						if(input[i][k] != '.') break;
					}
					if(k == -1) flag=1;
				}
				if(input[i][j] == 'v'){
					for(k = i+1; k < R; k++){
						if(input[k][j] != '.') break;
					}
					if(k == R) flag=1;
				}
				if(flag){
					if(!isit(i,j)){
						printf("IMPOSSIBLE\n");
						flag = 2;
						break;
					}
					ans++;
				}
			}
			if(flag==2)break;
		}
		if(flag==2)continue;
		printf("%d\n", ans);
	}

	return 0;
}

