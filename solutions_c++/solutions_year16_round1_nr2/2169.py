#include<stdio.h>
#include<cstring>
#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<map>

#define lld long long int
#define llu long long unsigned int
#define MAX 6

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
   char read[MAX];
   memset( read, 0, MAX );
   fscanf( fin, "%s", read );
   T = atoi( read );
   memset( read, 0, MAX );
   printf("%d\n",T);
   for( int x=1;x<=T;x++ )
   {
      int arr[2501]={0};
      fscanf( fin, "%s", read );
      int loop = atoi( read );
      //printf("%d\n",loop);
      int max = -1;
      for( int i=0; i<2*loop-1; i++ )
      {
         for( int j=0; j<loop; j++ )
         {
            fscanf( fin, "%s", read );
            int x = atoi(read);
            arr[x]++;
            if( max < x )
               max = x;
            //printf("%s ", read);
         }
         //printf("\n");
      }
      printf("max=%d\n",max);
      fprintf( fout, "Case #%d:",x );
      for( int i=1; i<=max; i++ )
      {
         //printf( " %d",i );
         if( arr[i] % 2 == 0 )
         {
            continue;
         }
         //printf( " %d",i );
         fprintf( fout, " %d",i );
      }
      fprintf( fout, "\n" );
      //printf( "\n" );
   }
   return 0;
}
