#include <stdio.h>
#include <stdlib.h>













// Funcion principal.

// Lee el archivo input ciclicamente hasta el final.
int main(void)
{
  //Variables.
  FILE * input=fopen("input.txt","r");
  FILE * output=fopen("output.txt","w");
  int T=0,i=0;
  //Leemos el número de casos.
  fscanf(input,"%d",&T);
  
  //Imprimos el numero de casos para comprobar.
  printf("\nNumero de casos a procesar: %d\n",T);
  
  //Procesa los T casos.
  for(i=0;i<=T-1;i++)
     { 
       //Por cada caso se leera: 1 respuesta + 4 lineas de cartas + 1 respuesta + 4 lineas de cartas.
       //Variables para input y para caso T.
       int answer1=0;
       int j=0,k=0;
       int answer2=0;
       int vector1[4];
       int vectoraux[4];
       int vector2[4];

       //Variables para output.
       int vectorI[4]={0,0,0,0};
       int Pos=0; //La cardinalidad sera la Pos+1.

       //Leemos la primera respuesta del voluntario 1.
       fscanf(input,"%d",&answer1);
       //Imprimimos la respuesta del voluntario 1.
       printf("\n Respuesta Voluntario 1: Fila # %d\n",answer1);
       //Leemos en un ciclo de 4 y solo guardamos la fila de la respuesta del voluntario 1.
       for(j=0;j<=3;j++)
          {
            if(j==(answer1-1)) 
              { 
                //Leemos la fila que nos interesa y la guardamos en vector 1.
                fscanf(input,"%d %d %d %d", &vector1[0], &vector1[1], &vector1[2], &vector1[3]);
                //Imprimimos los datos por consola para comprobar.
                printf(" \n Vector1: %d %d %d %d\n", vector1[0], vector1[1],vector1[2], vector1[3]);
              }
            else fscanf(input,"%d %d %d %d", &vectoraux[0], &vectoraux[1], &vectoraux[2], &vectoraux[3]);
          }
       //Leemos la respuesta del voluntario numero 2.
       fscanf(input,"%d", &answer2);
       //Imprimimos la respuesta del voluntario 2.
       printf("\n Respuesta Voluntario 2: Fila # %d\n",answer2);
       //Leemos en un ciclo de 4 y solo guardamos la fila de la respuesta del voluntario 2.
       for(j=0;j<=3;j++)
          {
            if(j==(answer2-1)) 
              { 
                //Leemos la fila que nos interesa y la guardamos en vector 1.
                fscanf(input,"%d %d %d %d", &vector2[0], &vector2[1], &vector2[2], &vector2[3]);
                //Imprimimos los datos por consola para comprobar.
                printf(" \n Vector2: %d %d %d %d\n", vector2[0], vector2[1],vector2[2], vector2[3]);
              }
            else fscanf(input,"%d %d %d %d", &vectoraux[0], &vectoraux[1], &vectoraux[2], &vectoraux[3]);
          }
        //Realizamos una comparacion de vectores
        for(j=0;j<=3;j++)
           {
             //Comparamos con cada elemento del vector 2.
             for(k=0;k<=3;k++)
                 {
                   if(vector1[j]==vector2[k]) 
                     {
                       vectorI[Pos]=vector1[j];
                       Pos++;
                       break; //Rompemos el for k.
                     }
                 }
           }
        //Determinamos el resultado con la cardinalidad.
        //imprimimos el vecor de interseccion.
        printf("\n #### Vector interseccion, variable Pos=%d", Pos);
        for(j=0;j<=3;j++)
           printf(" \n ### %d: %d",j,vectorI[j]);
     
       
        switch(Pos) // Cardinalidad=Pos+1.
         {
           case 0: printf("\n Volunteer cheated! \n");
                   fprintf(output,"Case #%d: Volunteer cheated!\n",i+1);
                   break;
           case 1: printf(" \n Tu carta es:%d \n", vectorI[0]);
                   fprintf(output,"Case #%d: %d\n",i+1,vectorI[0]);
                   break;
           default: printf(" \n Bad magician \n");
                   fprintf(output,"Case #%d: Bad magician!\n",i+1);
                   break;

         }

     }
  //Cerramos el archivo.
  fclose(input);
  return (0);
}
