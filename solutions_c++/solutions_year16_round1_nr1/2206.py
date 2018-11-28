#include<stdio.h>
#include<cstring>
#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<map>

#define print(n) printf("%llu\n",n)
#define lld long long int
#define llu long long unsigned int

using namespace std;

int main()
{
   FILE *fout,*fin;
   fout = fopen( "output.txt", "w" );
   if( NULL == fout )
   {
      printf("Not able to open file");
      return -1;
   }
   fin = fopen( "input.txt", "r" );
   if( NULL == fin )
   {
      printf("Not able to open file");
      return -1;
   }

   int T;
   char read[1020],outString[1020];
   memset( read, 0, 1020 );
   T = fscanf( fin, "%s", read );
   T = atoi( read );
   //printf("%d\n",T);
   for( int x=1;x<=T;x++ )
   {
      memset( read, 0, 1020 );
      fscanf(fin,"%s",read );
      outString[0] = read[0];
      char temp[1020];
      memset( temp, 0, 1020 );
      for( int i=1; i<strlen(read); i++ )
      {
         if( read[i] >= outString[0] )
         {
            strcpy( temp, outString );
            memset( outString, 0, 1020 );
            outString[0] = read[i];
            strcat( outString, temp );
            memset( temp, 0, 1020 );
            //printf("%s\n",outString); 
         }
         else
         {
            //printf("before=%s\n",outString);
            outString[strlen(outString)] = read[i];
            //printf("after=%s\n",outString);
         }
      }
      fprintf( fout, "Case #%d: %s\n",x,outString );
      //printf("%s\n",outString); 
      memset( outString, 0, 1020 );
   }
   return 0;
}
