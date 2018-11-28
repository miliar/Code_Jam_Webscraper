#include <stdio.h>

char matrix[5][5];

int ifwin(char x)
{
    int i, j, counter1 = 0, counter2 = 0;
    
     for(i = 0; i < 4; i++){
          for(j = 0; j < 4; j++){
                if(matrix[i][j] == x || matrix[i][j] == 'T') counter1++;
                if(matrix[j][i] == x || matrix[j][i] == 'T') counter2++;}
		  if(counter1 == 4 || counter2 == 4) return 1;
	      counter1 = counter2 = 0;}
    
     counter1 = 0;
    
     for(i = 0, j = 0; i < 4; i++, j++)
          if(matrix[i][j] == x || matrix[i][j] == 'T') counter1++;      
     if(counter1 == 4) return 1;
     
     counter1 = 0;
     
     for(i = 3, j = 0; i >= 0; i--, j++)
          if(matrix[i][j] == x || matrix[i][j] == 'T') counter1++;      
     if(counter1 == 4) return 1;
    
     return 0; 
}

int main()
{
    FILE *in = fopen("A-large.in", "r");
    FILE *out = fopen("out.out", "w"); 
    
    int cases, i, j, k, space_flag = 0;
    fscanf(in, "%d\n", &cases);
    
    for(i = 0; i < cases; i++)
    {
    	  space_flag = 0;
          for(j = 0; j < 4; j++){
               fscanf(in, "%s\n", matrix[j]);
               for(k = 0; k < 4; k++)
                      if(matrix[j][k] == '.') space_flag = 1; }
                
          if(ifwin('X')){
               fprintf(out, "Case #%d: X won\n", i+1); continue;}
          
          else if(ifwin('O')){
               fprintf(out,"Case #%d: O won\n", i+1); continue;}
          
          else
          {
              if(space_flag){
                    fprintf(out, "Case #%d: Game has not completed\n", i+1); continue;}
              else{
                    fprintf(out, "Case #%d: Draw\n", i+1); continue;}  
          }
    }
    return 0;
}
