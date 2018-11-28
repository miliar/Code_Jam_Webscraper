#include<stdio.h>
#include<conio.h>

int main(){
	 FILE* archivo;     FILE* archivo2;
    int aiTarjetas01[4][4];
    int aiTarjetas02[4][4];
    int aiFila01[] = {1, 2, 3, 4};
    int aiFila02[] = {1, 2, 3, 4};
	 archivo = fopen("A-small-attempt1.in", "r");
	 archivo2 = fopen("A-small-solution1.out", "w");
	 int iNro_Casos = 0;
	 if(archivo!=NULL){
		fscanf(archivo, "%d\n",
					&iNro_Casos);
		printf("\nNro. de Casos: %d", iNro_Casos);
		// Recorre todos los casos
		int iFila01 = 0; // Posicion de la primera fila
      int iFila02 = 0; // Posicion de la segunda fila
		for(int k = 1; k <= iNro_Casos; k++){
			// Leyendo la primera fila
			fscanf(archivo, "%d\n", &iFila01);

         //Lectura de las tarjetas
			printf("\nPrimera Fila: %d\n", iFila01) ;
         int iDato = 0;  int iLongitud = 4;
			for (int i = 0; i < iLongitud; i++){
         	for (int j = 0; j < iLongitud; j++){
					if (j == (iLongitud-1))  {
               	fscanf(archivo, "%d\n", &iDato);
                  printf("%d\n ", iDato);
               }
					else {
               	fscanf(archivo, "%d ", &iDato);
                  printf("%d ", iDato);
               }
					aiTarjetas01[i][j]=iDato;

         	}
			}
			// Leyendo la segunda fila
			fscanf(archivo, "%d\n", &iFila02);
			printf("\nPrimera Fila: %d\n", iFila02) ;

			for (int i = 0; i < iLongitud; i++){
         	for (int j = 0; j < iLongitud; j++){
					if (j == (iLongitud-1))  {
               	fscanf(archivo, "%d\n", &iDato);
                  printf("%d\n ", iDato);
               }
					else {
               	fscanf(archivo, "%d ", &iDato);
                  printf("%d ", iDato);
               }
					aiTarjetas02[i][j]=iDato;
            }
			}

			//llenar los arreglos de las filas

			for(int j=0;j<iLongitud;j++)
			{
         	aiFila01[j] = aiTarjetas01[iFila01-1][j];
            printf("%d ", aiFila01[j]);
			}
         for(int j=0;j<iLongitud;j++)
			{
         	aiFila02[j] = aiTarjetas02[iFila02-1][j];
            printf("%d ", aiFila02[j]);
			}
         // Buscando
         int iEncontrados = 0; int iTarjeta = 0;
			for(int i=0;i<iLongitud;i++)
			{
				for(int j = 0; j < iLongitud; j++)
				{
					if(aiFila01[i] == aiFila02[j])
					{
						iEncontrados++; iTarjeta = aiFila01[i];
					}
				}
			}
         printf("Encontrados %d %d ", iEncontrados, iTarjeta);

         char *respuesta = "";
         if (iEncontrados == 0){
         	respuesta =  "Volunteer cheated!";
            fprintf(archivo2, "Case #%d: %s\n", k, respuesta);
         }
         if (iEncontrados == 1){

            fprintf(archivo2, "Case #%d: %d\n", k, iTarjeta);
         }
         if (iEncontrados > 1){
         	respuesta = "Bad magician!";
            fprintf(archivo2, "Case #%d: %s\n", k, respuesta);
         }
         printf("\n");
			printf("%s\n ",respuesta);
			printf("\n");

		} // Fin de for k
		fclose(archivo);  fclose(archivo2);
      getch();
	 } // Fin de if(archivo!=NULL)
}
