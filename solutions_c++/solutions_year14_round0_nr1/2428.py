#include <stdio.h>

using namespace std;

int Odw[20];

int main(){
	int t;
	int i,j,k,ile,ktory,w1,liczba;
	scanf("%d", &t);
	for(i=0; i<t; i++){
		for(j=0; j<20; j++) Odw[j] = 0;
		scanf("%d", &w1);
		for(j=1; j<=4; j++){
			for(k=1; k<=4; k++){
				scanf("%d", &liczba);
				if( j==w1 ) Odw[liczba]++;
			}
		}
		scanf("%d", &w1);
		for(j=1; j<=4; j++){
			for(k=1; k<=4; k++){
				scanf("%d", &liczba);
				if( j==w1 ) Odw[liczba]++;
			}
		}
		ile = 0;
		for(j=0; j<20; j++) {
			if( Odw[j] == 2 ) {
				ktory = j;
				ile++;
			}
		}
		if(ile == 0) printf("Case #%d: Volunteer cheated!\n", i+1);
		if(ile == 1) printf("Case #%d: %d\n", i+1,ktory);
		if(ile > 1) printf("Case #%d: Bad magician!\n", i+1);
	}
	return 0;
}
