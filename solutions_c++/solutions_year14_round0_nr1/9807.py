#include <stdio.h>

int main()
{	
	int t;
    int row[4];
    int count;
    int card;
    		
    FILE *in = fopen ("A-small-attempt0.in","r");
    FILE *out = fopen ("a.out","w");
    
	fscanf (in,"%d",&t);
	
    int answ;
    int help;	

	for (int i = 1; i <= t; i++) {
      count = 0;
      
	  fscanf (in,"%d",&answ);
	  
	  for (int j=1; j <= 4; j++) {
         for (int q =0; q < 4; q++) {
            fscanf (in,"%d",&help);
            if (j == answ) row[q] = help;
         }
      }
	  fscanf (in,"%d",&answ);

      for (int j=1; j <= 4; j++) {
         for (int q =0; q < 4; q++) {
            fscanf (in,"%d",&help);
            if (j == answ) {
              for (int k = 0; k < 4; k++)
                if (row[k] == help) {card=help; count++;}
            }
         }
      }
      	  
	  fprintf (out,"Case #%d: ",i);
	  
	  if (count == 1) 
        fprintf (out,"%d",card);
      else if (count == 0)
        fprintf (out,"Volunteer cheated!");
      else
        fprintf (out,"Bad magician!"); 

	  if (i < t) fprintf(out,"\n");
    }    
    
    fclose (in);
    fclose (out);
}
