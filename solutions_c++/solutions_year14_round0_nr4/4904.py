#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	int T;
	scanf ("%d", &T);
	for (int t = 0; t < T; t++){
		int N;
		scanf("%d", &N);
		float naomi[10], ken[10];
		
		for (int i = 0; i < N; i++){
			scanf("%f", &naomi[i]);
		}
		for (int j = 0; j < N; j++){
			scanf("%f", &ken[j]);
		}
		
		for (int i = 0; i < N; i++){
			for (int j = 0; j < i; j++){
				if (naomi[i]<naomi[j]){
					float c = naomi[i];
					naomi[i] = naomi[j];
					naomi[j] = c;
				}
				if (ken[i]<ken[j]){
					float c = ken[i];
					ken[i] = ken[j];
					ken[j] = c;
				}
			}
		}
		
		//war
		
		int j = -1;
		int war = 0;
		for (int i = 0; i < N; i++){
			while (j < N - 1){
				j++;
				if (naomi[i] < ken[j]){
					war ++;
					break;
				}					
			}
		}
		
		//deceitful War
		int dwar[N];
		
		for (int i = 0; i < N; i++){
			dwar[i] = 0;
			//žrtvuje do i.tega iz tega seznama in pobija od zadaj naprej
			for (int j = 0; j < i; j++){
				if (naomi[j]>ken[N-j-1]) dwar[i]++;
			}
			for (int j = i; j < N; j++){
				if (naomi[j]>ken[j-i]) dwar[i]++;
			}	
		}
		
		for (int i = 0; i < N; i++){
			for (int j = 0; j < i; j++){
				if (dwar[i]>dwar[j]){
					float c = dwar[i];
					dwar[i] = dwar[j];
					dwar[j] = c;
				}
			}
		}
		
		printf("Case #%d: %d %d", t+1, dwar[0], N - war);
				
			
		printf("\n");
		
		
	}
	return 0;	
}