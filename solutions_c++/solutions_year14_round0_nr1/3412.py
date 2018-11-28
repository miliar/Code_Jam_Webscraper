#include <stdio.h>

main(){
	int T, M1[5][5], M2[5][5], i, j, caso, a, b, L1[5], L2[5], iguais, resp;
	
	
	scanf("%d", &T);
	
	for (caso=1;caso<=T;caso++)
	{
		scanf("%d", &a);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d", &M1[i][j]);
				if(a==i)
					L1[j]=M1[i][j];
			}
		}

		scanf("%d", &b);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d", &M2[i][j]);
				if(b==i)
					L2[j]=M2[i][j];
			}
		}
		
		
		iguais=0;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				if(L1[i]==L2[j]){
					iguais++;
					resp=L1[i];
				}
			}
		}
			
		printf("Case #%d: ", caso);
		
		if(iguais==1)
			printf("%d\n", resp);
		else if (iguais >1)
			printf("Bad magician!\n");
		else if (iguais == 0)
			printf("Volunteer cheated!\n");
	}
}
