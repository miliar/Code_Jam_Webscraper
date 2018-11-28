#include <cstdio>

using namespace std;

int Odw[11];

int main(){
	int t,i,n,j;
	int x,y,ile;
	scanf("%d", &t);
	for(i=0; i<t; i++){
		scanf("%d", &n);
		if(n == 0){
			printf("Case #%d: INSOMNIA\n", i+1);
			continue;
		}
		ile = 0;
		for(j=0; j<=9; j++) Odw[j] = 0;
		x =  n;
		while(ile != 10){
			y = x;
			while(y>0){
				Odw[y%10]++;
				if(Odw[y%10] == 1) ile++;
				y /= 10;
			}
			x += n;
		}
		printf("Case #%d: %d\n", i+1,x-n);
	}
	return 0;
}
