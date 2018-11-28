#include <stdio.h>

using namespace std;

int game(int a);

int main(){
	int cases, low, high, tmp;

	scanf("%d", &cases);
	for(int i=0; i<cases; i++){
		printf("Case #%d: ", (i+1));
		scanf("%d %d", &low, &high);
		tmp = game(high) - game(low-1);
		printf("%d\n", tmp);
	}

	return 0;
}

int game(int a){
	if(a>=484)
		return 5;
	if(a>=121)
		return 4;
	if(a>=9)
		return 3;
	if(a>=4)
		return 2;
	if(a>=1)
		return 1;
	return 0;
}
