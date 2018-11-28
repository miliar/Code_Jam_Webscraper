#include<cstdio>

#define n 4

int row, x, caso, C;

void doCase(){
	scanf("%d", &row);
	--row;

	int mask = 0;
	
	for(int i = 0; i < n ; ++i)
		for(int j = 0; j < n ; ++j){
			scanf("%d",&x); --x;
			if(i == row)mask ^= (1 << x);
		}

	scanf("%d", &row);
	--row;

	int count = 0;
	int ans = -1;
	for(int i = 0; i < n ; ++i)
		for(int j = 0; j < n ; ++j){
			scanf("%d",&x);--x;
			if( i == row &&  ( (mask >> x) & 1 ) )++count, ans = x;
		}

	if(count == 0)printf("Case #%d: Volunteer cheated!\n", ++caso);
	else if(count == 1)printf("Case #%d: %d\n", ++caso, ans + 1);
	else printf("Case #%d: Bad magician!\n", ++caso);
		
}

int main(){
	caso = 0;
	scanf("%d",&C);
	for(int i = 0; i < C; ++i)doCase();
}
