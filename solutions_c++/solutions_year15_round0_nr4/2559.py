#include <cstdlib>
#include <cstdio>

int main()
{
	int T, n, i, j, k, x, r, c, ans, now;
	int p[1005];
	scanf("%d", &T);
	for(i = 0; i < T; i++){
		scanf("%d %d %d", &x, &r, &c);
		if(x == 1){
			printf("Case #%d: GABRIEL\n",i+1);// G means no matter what grids can be filled
			continue;
		}
		if(x == 2){
			if(r*c%2 == 0)
				printf("Case #%d: GABRIEL\n",i+1);
			else
				printf("Case #%d: RICHARD\n",i+1);
			continue;
		}
		if(x == 3){
			if((r*c%3==0) && (r*c>3))
				printf("Case #%d: GABRIEL\n",i+1);
			else
				printf("Case #%d: RICHARD\n",i+1);
			continue;
		}
		if(x == 4){
			if(r*c == 12 || r*c == 16)
				printf("Case #%d: GABRIEL\n",i+1);
			else
				printf("Case #%d: RICHARD\n",i+1);
			continue;
		}

	}
}

