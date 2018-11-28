#include <stdio.h>

int main(int argc, const char* argv[]) {
	
	int numtests;
  int casenum = 0;
  int result;
  int X, R, C;

	//printf("ENTER NUMBER OF TEST CASES: ");
	scanf("%d", &numtests);

	while(++casenum <= numtests) {
    

    // 1 = Richard
    // 0 = Gabriel

    //reset result
    result = 0;

    // Reads in params
    scanf("%d", &X);
    scanf("%d", &R);
    scanf("%d", &C);


    // Check for 1-omino .. Gabriel will win fo sho
    if (X == 1)
      result = 0;

    // Check for area .. if no more space Richard will win
    else if (X > R*C || (X > R  && X > C) || ( X - 1 > R || X - 1 > C ))
      result = 1;

    // Checks for area mod .. if not 0 then Richard will win 
    else if ((R*C) % X != 0) 
      result = 1;

    else {

      if (X % 2 == 1)
        X++;

      //if (X / 2 - 1 >= R || X/2 - 1 >= C)
      if (X / 2 - 1 >= R || X/2 - 1 >= C) 
        result = 1;
      /*
      else {
        //else {
          
          for (int i = 1, j = X - 1; i <= (int)(X / 2); i++, j--) {
            
            if (i * j == X) {
      
              if ((i > C && i < R) || (i > R && i < C)) {
                
                result = 1;
                i = X;
              }
            }
            
          }
      
        //}

      }
      */

      /*
      for (int r = 1, c = X - 1; r < X; r++, c++) {
        if (r >= R/2 && c >= C/2) 
          result = 1;
        else result = 0;
      } */
    }
    // Checks for width
    /*
    else {
      
      for (int i = 1; i <= (int)(X / 2); i++) {
        
        if (X % i == 0) {
  
          if ((i > C && i < R) || (i > R && i < C)) {
            
            result = 1;
            i = X;
          }
        }
        
      }
  
    }
    */


		// Print case num and needed nums
    if (result)
      printf("Case #%d: RICHARD\n", casenum);	
	  
    else
      printf("Case #%d: GABRIEL\n", casenum);

  }


}
