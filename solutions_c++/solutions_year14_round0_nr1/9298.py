#include<cstdio>
int main(){
    int cont=1,t, carta;
    scanf("%d", &t);
    while(cont<=t){
        int res, contVer=0;
        scanf("%d", &res);
        int arranjo[4][4];
        int vetValues[4];
        for(int x=0; x<4; x++)for(int y=0; y<4; y++) scanf("%d", &arranjo[x][y]);
        for(int i=0; i<4; i++) vetValues[i]=arranjo[res-1][i];
        scanf("%d", &res);
        for(int x=0; x<4; x++)for(int y=0; y<4; y++) scanf("%d", &arranjo[x][y]);
	    for(int i=0; i<4; i++){
	         for(int mati=0; mati<4; mati++){
		        if(vetValues[i]==arranjo[res-1][mati]){
		                contVer++;
		                carta=vetValues[i];
		        }
	        }
        }
        if(contVer==0) printf("Case #%d: Volunteer cheated!\n", cont);
        if(contVer>1) printf("Case #%d: Bad magician!\n", cont);
        if(contVer==1) printf("Case #%d: %d\n", cont, carta);
        cont++;
    }
    return 0;
}
