#include <stdio.h>
int main () {
  int t;    
  int smax;  
  char p;
  
  FILE* fin = fopen("A-large.in","r");
  FILE* fout = fopen("a.out","w"); 
  
  
  fscanf (fin,"%d",&t);
  
  for (int i =1; i <= t; i++) {
    fscanf (fin,"%d",&smax);
	fscanf (fin,"%c",&p);        
        
    int people = 0;
    int sol = 0;
    
    for (int j = 0; j <= smax; j++) {
      fscanf (fin,"%c",&p);      
      
      if (people >= j) 
        people = people + (p - '0');
      else {
        sol = sol + (j-people);
        people = j + (p - '0');
      }
    }                        
    
    fprintf (fout,"Case #%d: %d\n",i,sol);
  }
  
  fclose (fin);
  fclose (fout);
  
  return 0;
}
