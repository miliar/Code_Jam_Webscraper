#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>

char T4[4][4];


   char Wins[][5] = { "TXXX" , "XTXX" , "XXTX" , "XXXT" , "XXXX" , "TOOO" , "OTOO" , "OOTO" , "OOOT" , "OOOO" };



int solve() {
   char T4_2[][5] = { "     " , "     " , "     " , "     " , "     " , "     " , "     " , "     " , "     " , "     " };
	int result = 0;

	int is_not_complet = 0;

   		for(int i = 0 ; i<4 ;i++){
      	for(int j = 0 ; j<4 ;j++){
           if(T4[i][j] == '.'){
           		is_not_complet = 1;
               break;
           }
         }
      }


		for(int i = 0 ; i<10 ;i++){

      	if(i<4){

         	T4_2[i][0] = T4[i][0];    T4_2[i][1] = T4[i][1];
         	T4_2[i][2] = T4[i][2];    T4_2[i][3] = T4[i][3];

         }else if(i<8){

            T4_2[i][0] = T4[0][i%4];    T4_2[i][1] = T4[1][i%4];
         	T4_2[i][2] = T4[2][i%4];    T4_2[i][3] = T4[3][i%4];

         }else{
           if(i == 8){
         		T4_2[i][0] = T4[0][0];    T4_2[i][1] = T4[1][1];
         		T4_2[i][2] = T4[2][2];    T4_2[i][3] = T4[3][3];
           }else{

           		T4_2[i][0] = T4[0][3];    T4_2[i][1] = T4[1][2];
         		T4_2[i][2] = T4[2][1];    T4_2[i][3] = T4[3][0];

           }
         }

      }


 int number;

      for(int i=0; i<10 ; i++){

      	for(int j=0; j<10 ; j++){

          if( strncmp (T4_2[i],Wins[j],4) == 0){
          	result = 1;
            number = j;
           goto LABEL1;
          }

         }
      }
      
LABEL1:

	if (result != 0){
		result = (number<5) ? 1 : 2;
	}else{
	   result = (is_not_complet == 1) ? 4 : 3;
}

	return result;

}



int main(){

	int T;
   char L_T;

FILE *input_file;
FILE *output_file;

	if ( (input_file = fopen( "A-large.in", "r" )) != NULL ){

      output_file = fopen( "A-large.out", "w" );

      	fscanf(input_file, "%d ", &T);

         	for(int i=1 ; i <= T ; i++ ){

            		for(int j = 0 ; j<4 ;j++){
                		fscanf(input_file, "%c %c %c %c", &T4[j][0], &T4[j][1], &T4[j][2], &T4[j][3]);
                     fscanf(input_file, "%c", &L_T);
                	}

                  fscanf(input_file, "%c", &L_T);

            switch(solve()){

            	case 1:
               	fprintf(output_file,"Case #%d: X won\n",i);
               break;

               case 2:
               	fprintf(output_file,"Case #%d: O won\n",i);
               break;

               case 3:
               	fprintf(output_file,"Case #%d: Draw\n",i);
               break;

               case 4:
               	fprintf(output_file,"Case #%d: Game has not completed\n",i);
               break;

            }
      }

      fclose(input_file);
      fclose(output_file);

   }else{

		printf("Error Opening File");
      getch();
      exit(1);

	}
	return 0;
}

