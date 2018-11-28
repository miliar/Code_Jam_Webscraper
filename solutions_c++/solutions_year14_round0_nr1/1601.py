#include <cstdio>
#include <cstdlib>

int main(){
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		int m[4][4];
		int v[17];
		int a;
		scanf("%d", &a);
		for(int i = 0; i < 17; i++)
			v[i] = 0;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				scanf("%d", &m[i][j]);
		for(int i = 0; i < 4; i++)
			v[m[a-1][i]]++;
		scanf("%d", &a);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				scanf("%d", &m[i][j]);
		for(int i = 0; i < 4; i++)
			v[m[a-1][i]]++;
		int r = 0;
		for(int i = 1; i <= 16; i++){
			if(v[i] == 2 && r == 0)
				r = i;
			else if(v[i] == 2 && r > 0)
				r = -1;
		}
		printf("Case #%d: ", t);
		if(r > 0)
			printf("%d\n", r);
		if(r == 0)
			printf("Volunteer cheated!\n");
		if(r < 0)
			printf("Bad magician!\n");
	}
	return 0;
}
