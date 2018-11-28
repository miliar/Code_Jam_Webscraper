#include <stdio.h>
#include <stdlib.h>



int main( void )
    {
      //Variables para los resultados.
      FILE * input=fopen("input.txt","r");
      FILE * output=fopen("output.txt","w");     
      int T=0,i=0;

      // Se lee el numero de casos T.
      fscanf(input,"%d",&T);

      //Imprimimos en consola el numero de casos.
      printf("\n Numero de casos: %d\n",T);

      //Realizamos en un for para cada caso.
      for(i=0;i<=T-1;i++)
        {
          //Variables para cada caso.
          double C,F,X,GS=2.0,TS=0.0; 
          double res1, res2, Menor;         
          int Iteraciones=0,j=0,k=0;

          // Se leen las variables.
          fscanf(input,"%lf %lf %lf",&C,&F,&X);

          // Se muestran en consola para verificar.
          printf("\n C=%f\tF=%f\tX=%f\n",C,F,X);

          //Se calculan las iteraciones.
          Iteraciones=X;

          //Se muestra en pantalla el numero de iteraciones.
          printf("\n Numero de iteraciones=%d\n",Iteraciones);

              
          //Calculamos para Iteraciones sera el caso Base.
          for(j=1;j<=Iteraciones;j++) 
                { 
                  TS+=C/GS;                  
                  GS+=F;                  
                }
          TS+=X/GS;
          Menor=TS;
           
          //Calculamos las demas posibilidades Iteraciones -1;
          for(k=Iteraciones;k>=0;k--)
             {
               //Todo.

               //Reseteamos las variables a usar.
               TS=0.0;            
               GS=2.0;
  
               //Calculamos para k posibilidad.
               for(j=1;j<=k;j++) 
                  { 
                    TS+=C/GS;                  
                    GS+=F;                  
                  }
               TS+=X/GS;

               //Checamos si el nuevo calculo es menor que la clase base.
               if( TS<Menor ) Menor=TS;
             }            
            
          //Imprimos resultados.
          printf("\n #### Total segundos: %.7f\n",Menor);
          fprintf(output,"Case #%d: %.7f\n",i+1,Menor);           
       }

      return(0);
    } 
