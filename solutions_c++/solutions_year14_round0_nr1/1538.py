#include <cstdio>

int T;
int ans, cand[2][4];

bool exist(int p, int v) 
{
	for(int i=0;i<4;i++) if(cand[p][i] == v) return true;
	return false;
}

int main()
{
	scanf("%d", &T);
	for(int t=0;t++<T;){
		scanf("%d", &ans);
		for(int i=1;i<=4;i++){
			for(int j=0;j<4;j++){
				int v; scanf("%d", &v);
				if(ans == i) cand[0][j] = v;
			}
		}
		scanf("%d", &ans);
		for(int i=1;i<=4;i++){
			for(int j=0;j<4;j++){
				int v; scanf("%d", &v);
				if(ans == i) cand[1][j] = v;
			}
		}

		int ret = -1;
		for(int i=1;i<=16;i++){
			if(exist(0, i) && exist(1, i)){
				if(ret == -1) ret = i;
				else ret = -2;
			}
		}

		printf("Case #%d: ", t);
		if(ret == -1) puts("Volunteer cheated!");
		else if(ret == -2) puts("Bad magician!");
		else printf("%d\n", ret);
	}
	return 0;
}
