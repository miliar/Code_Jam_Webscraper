#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc,char** argv){
	int tamanho,i=0,max,amigos,empe,j=0,temp=0;
	char vetor[1001];
	FILE *arqOutput;
	FILE *arqInput;
	arqInput=fopen(argv[1],"r");
	arqOutput=fopen(argv[2],"w");
	if(arqInput==NULL||arqOutput==NULL){
		printf("Falha no acesso aos arquivos");
		exit(42);
	}
	memset(vetor,0x00,sizeof(vetor));
	fscanf(arqInput,"%d",&tamanho);
	for(i=0;i<tamanho;i++){
		max=0;
		fscanf(arqInput,"%d",&max);
		printf("teste i %d max %d\n",i,max);
		empe=0;
		amigos=0;
		j=0;
		fscanf(arqInput," %c",&vetor[j]);
		temp=vetor[j]-'0';
		if(temp){
			empe+=temp;
		}
		for(j=1;j<=max;j++){
			fscanf(arqInput," %c",&vetor[j]);
			temp=vetor[j]-'0';
			printf("   teste j %d\n",j);
			if(temp){					
				if(empe<j){
					amigos+=(j-empe);
					empe+=amigos;
				}
				empe+=temp;
			}
			printf("      amigos %d empe %d\n",amigos,empe);
		}
		fprintf(arqOutput,"Case #%d: %d\n",i+1,amigos);
	}
	return 0;
}
