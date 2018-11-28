#include <stdio.h>

int casos,fila,tabla[4][4],posibles[4],lugar,cuenta;

void lee(){
	scanf("%d",&fila);
	for(int i = 0;i < 4;i++)
		for(int j = 0;j < 4;j++)
			scanf("%d",&tabla[j][i]);
	fila--;
}
void llenaPosibles(){
	for(int i = 0;i < 4;i++){
		posibles[i] = tabla[i][fila];
	}
}
int checa(){
	int r = 0;
	for(int i = 0;i < 4;i++){
		for(int j = 0;j < 4;j++){
			if(tabla[i][fila] == posibles[j]){
				lugar = j;
				r++;
			}
		}
	}
	return r;
}
int main(){
	freopen("in.txt","r",stdin);
	scanf("%d",&casos);
	for(int i = 0;i < casos;i++){
		lee();
		llenaPosibles();
		lee();
		printf("Case #%d: ",i+1);
		cuenta = checa();
		if(cuenta == 0)
			printf("Volunteer cheated!\n");
		else if(cuenta == 1)
			printf("%d\n",posibles[lugar]);
		else
			printf("Bad magician!\n");
	}
	return 0;
}
