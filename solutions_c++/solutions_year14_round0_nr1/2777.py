#include <stdio.h>


int main(){
    int T; scanf("%d", &T);

    for (int Tcount = 1; Tcount <= T; Tcount++)
    {
    	int A, B[4][4],C,D[4][4];
    		scanf("%d",&A);
    		for(int i=0;i<4;i++)
    			for(int j=0;j<4;j++)
    				scanf("%d",&B[i][j]);
    		scanf("%d",&C);
    		for(int i=0;i<4;i++)
    			for(int j=0;j<4;j++)
    				scanf("%d",&D[i][j]);
    		int E=0;
    		for (int i = 0; i < 4; i++)
    		{
    			for (int j = 0; j < 4; j++)
    			{
                if(B[A-1][i]==D[C-1][j]){
                    if(E==0)
                        E=B[A-1][i];
                    else
                        E=42;
                    }
    			}
    		}
    printf("Case #%d: ", Tcount);
    		if (E==42){
    			printf("Bad magician!\n");
    		}
    		else if(E==0){
    			printf("Volunteer cheated!\n");
    		}
    		else
    			printf("%d\n",E);


    }
    return 0;

}