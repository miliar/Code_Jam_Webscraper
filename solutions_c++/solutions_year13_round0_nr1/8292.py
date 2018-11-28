#include <iostream>
char ifile[] = "c:\\A-small-attempt0.in";
char ofile[] = "c:\\a.out";

void main() {
   FILE *ifp = fopen(ifile,"r");
   FILE *ofp = fopen(ofile,"w");

   if (ifp == NULL)
      printf("Error, input file");
   if(ofp == NULL)
      printf("Error output file");

 
   int N;
   char M[4][4];

   int R[4];
   int C[4];
   char Dot;
   int D[2];
   int X;
   int Oh;
   char W;
   char eol;

   int i,r,c;
   fscanf(ifp,"%d%c",&N,&eol);

   for(i = 0; i<N; i++) {

      R[0]=0;R[1]=0;R[2]=0;R[3]=0;
      C[0]=0;C[1]=0;C[2]=0;C[3]=0;
      D[0]=0;D[1]=0;
      Dot = 0;
      X = 0;
      Oh = 0;
      W = 0;

     for(r=0;r<4;r++)  {
         for(c=0;c<4;c++)  {
            M[r][c] = 0;
         }
     }

      for(r=0;r<4;r++)  {
         for(c=0;c<4;c++)  {
            fscanf(ifp,"%c",&M[r][c]);
            R[r] = R[r]+ M[r][c];
            C[c] = C[c]+ M[r][c];

            if(r == c)
               D[0] = D[0] + M[r][c];
            if (r+c == 3)
               D[1] = D[1] + M[r][c];

            if( (M[r][c]) == '.' )
               Dot = M[r][c];

            printf("%c",M[r][c]);
         }
         printf("\n");
         fscanf(ifp,"%c",&eol);

         if( (R[r] == ('X' * 4) ) || (R[r] == ('X' * 3) + 'T' ) )
            W = 'X' ;

         if( (R[r] == ('O' * 4) ) || (R[r] == ('O' * 3) + 'T' ) )
            W = 'O' ;

         if( r == 3) {
            if( (D[0] == ('X' * 4) ) || 
                (D[0] == ('X' * 3) + 'T' ) || 
                (D[1] == ('X' * 4) ) || 
                (D[1] == ('X' * 3) + 'T' ) )   {
               W = 'X';
            } else if( (D[0] == ('O' * 4) ) || 
               (D[0] == ('O' * 3) + 'T' ) || 
               (D[1] == ('O' * 4) ) || 
               (D[1] == ('O' * 3) + 'T' ) )   {
               W = 'O' ;
            }
         }
      }

      for(c=0;c<3;c++)  {
         if( (C[c] == ('X' * 4) ) || (C[c] == ('X' * 3) + 'T' ) )
            W = 'X' ;

         if( (C[c] == ('O' * 4) ) || (C[c] == ('O' * 3) + 'T' ) )
            W = 'O' ;
      }

      if ( W != 0)   {
         fprintf(ofp,"Case #%d: %c won\n",i+1,W);
      }
      else  if (Dot != 0)  {
         fprintf(ofp,"Case #%d: Game has not completed\n",i+1);
      }
      else  {
         fprintf(ofp,"Case #%d: Draw\n",i+1);
      }

      printf("\n");
      fscanf(ifp,"%c",&eol);

   }
   fclose(ifp);
   fclose(ofp);



}
