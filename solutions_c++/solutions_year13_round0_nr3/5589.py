#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <math.h>


int palindrome(int A){

	 int reverse = 0;

   while (A != 0)
   {
      reverse = reverse * 10;
      reverse = reverse + A%10;
      A = A/10;
   }

   return reverse;
}



int solve(int A, int B) {

 int result = 0;
 float temp_1;
 int temp_2;

    for (int n = A; n <= B; n++) {

    	if(n == palindrome(n)){

      	temp_1 =  sqrt (n);

         if(ceil(temp_1) == temp_1){

            temp_2 = (int)temp_1;

            if(temp_2 == palindrome(temp_2)){	result++;   }

         }
      }
    }

    return result;
}





int main(){

	int T;
   int A,B;

FILE *input_file;
FILE *output_file;

	if ( (input_file = fopen( "C-small.in", "r" )) != NULL ){

      output_file = fopen( "C-small.out", "w" );

      //Reading Nomber of test cases from  file

      	fscanf(input_file, "%d", &T);

        for(int i=1 ; i <= T ; i++ ){

      			fscanf(input_file, "%d %d", &A, &B);
               fprintf(output_file,"Case #%d: %d\n",i, solve(A,B));

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

