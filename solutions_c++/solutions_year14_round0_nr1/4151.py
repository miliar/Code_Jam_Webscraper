#include <cstdio>
using namespace std;

int N=4, TC;


int main(){
	scanf("%d",&TC);
	for(int tc=1; tc<=TC; ++tc){

		int pres[17]={0};
		int r, t, pos=0;

		scanf("%d",&r);
		for(int i=0; i<N; ++i){
			for(int o=0; o<N; ++o){
				scanf("%d",&t);
				if( i+1 == r ) ++pres[t];
			}
		}
		
		scanf("%d",&r);
		for(int i=0; i<N; ++i){
			for(int o=0; o<N; ++o){
				scanf("%d",&t);
				if( i+1 == r && pres[t] ){
					++pos;
					++pres[t];
				}
			}
		}

		printf("Case #%d: ",tc);
		if( pos == 1 ){
			for(int i=1; i<=16; ++i){
				if( pres[i] == 2 ){
					printf("%d",i);
					break;
				}
			}
		}
		else if( pos > 1 ){
			printf("Bad magician!");
		}
		else if( pos == 0 ){
			printf("Volunteer cheated!");
		}
		printf("\n");

	}
	return 0;
}
