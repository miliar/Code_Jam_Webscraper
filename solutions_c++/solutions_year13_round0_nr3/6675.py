#include <iostream>
//char ifile[] = "c:\\A-large.in";
char ifile[] = "c:\\C-small-attempt0.in";
//char ifile[] = "c:\\A-small-attempt1.in";
//char ifile[] = "c:\\A-small-attempt2.in";
//char ifile[] = "c:\\A-large.in";
//char ifile[] = "c:\\test.in";
char ofile[] = "c:\\a.out";

void main() {
   FILE *ifp = fopen(ifile,"r");
   FILE *ofp = fopen(ofile,"w");
   char eol;
   int database[5] = {1,4,9,121,484};

   if (ifp == NULL)
      printf("Error, input file");
   if(ofp == NULL)
      printf("Error output file");

 
   int T, num;

   int A,B;
   fscanf(ifp,"%d%c",&T,&eol);
   printf("Cases = %d\n",T);

   for(int i = 1; i<= T; i++) {
      fscanf(ifp,"%d%d",&A,&B);
      printf("low = %d, high = %d\n",A,B);
      num = 0;
      for(int j = 0; j < 5; j++) {
         if ( ( database[j] >= A ) && (( database[j] <= B )) )
            num++;
      }

      fprintf(ofp,"Case #%d: %d\n",i, num);
   }


   fclose(ifp);
   fclose(ofp);
   ifp = NULL;
   ofp = NULL;

}
