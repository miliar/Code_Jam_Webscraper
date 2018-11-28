#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int main(){
	 FILE* archivo;     FILE* archivo2;
    int nTopeNivel = 0;
	 int nInvitados = 0; int nAplauden = 0; int nAudienciaNivel = 0;
    int nInvitadosNivel = 0;
    char texto[100];
	 archivo = fopen("A-small-attempt0.in", "r");
	 archivo2 = fopen("A-small-attempt0.out", "w+");
	 int iNro_Casos = 0;
	 if(archivo!=NULL){
		fscanf(archivo, "%d\n",
					&iNro_Casos);
		printf("\nNro. de Casos: %d \n", iNro_Casos);
		// Recorre todos los casos

		for(int k = 1; k <= iNro_Casos; k++){
			// Leyendo Datos
			fscanf(archivo, "%d \n", &nTopeNivel);
         fscanf(archivo, "%s \n", &texto);
         printf("%d %s \n", nTopeNivel, texto);

         nInvitados = 0; nAplauden = 0; nAudienciaNivel = 0;
         int i = 0;
         printf("nTopeNivel = %d \n", nTopeNivel);
         while (i <= nTopeNivel){
         	printf("while (i < nTopeNivel) i= %d \n", i);
            char nivel = texto[i]; //char nivel[1];  nivel = texto.substr(i, 1);

         	nAudienciaNivel = nivel; nAudienciaNivel -= 48;
            printf("nAudienciaNivel = %d \n", nAudienciaNivel);
            if (nAudienciaNivel > 0){
            	if ( nAplauden < i ){
            		nInvitadosNivel = i - nAplauden;
            		nAplauden += nInvitadosNivel + nAudienciaNivel;
                  printf("if ( nAplauden < i ) %d \n", nAplauden);
               }
            	else{
            		nAplauden += nAudienciaNivel;
	            	nInvitadosNivel = 0;
                  printf("if-else ( nAplauden < i ) %d \n", nAplauden);
            	}
            }
            else{
            	nInvitadosNivel = 0;
            }
				nInvitados += nInvitadosNivel;
            printf("Invitados %d \n", nInvitados);
            i++;
         }

         //printf("Invitados %d \n", nInvitados);
         fprintf(archivo2, "Case #%d: %d\n", k, nInvitados);

		} // Fin de for k
		fclose(archivo);  fclose(archivo2);
      getch();
	 } // Fin de if(archivo!=NULL)
}


