#include<cstdio>
#include<cstdlib>
using namespace std;

int wiersze[102];
int kolumny[102];
int T[102][102];

int main(){
	int Z;
	scanf("%d", &Z);
	for(int t=1; t<=Z; t++){
		int w, k;
		scanf("%d %d", &w, &k);
		for(int i=0; i<w; i++)
			for(int j=0; j<k; j++)
				scanf("%d", &T[i][j]);
		for(int i=0; i<k; i++)
			kolumny[i] = 0;
		for(int i=0; i<w; i++)
			wiersze[i] = 0;		
		for(int i=0; i<w; i++)
			for(int j=0; j<k; j++){
				if(wiersze[i] < T[i][j])
					wiersze[i] = T[i][j];
				if(kolumny[j] < T[i][j])
					kolumny[j] = T[i][j]; 
			}
		bool skonczone = false;
		for(int i=0; i<w; i++){
			for(int j=0; j<k; j++)
				if(T[i][j] < kolumny[j] && T[i][j] < wiersze[i]){
					skonczone = true;
					printf("Case #%d: NO\n", t);
					break;
				}				
			if(skonczone)
				break;
		}
		if(!skonczone)
			printf("Case #%d: YES\n", t);
	}
	return 0;
}
