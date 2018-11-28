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

bool correctArray( bool *a )
{
   for( int i=0; i<10; i++ )
   {
      if( !a[i] )
      {
         return false;
      }
   }
   return true;
}

void getDigits( lld val, bool *arr )
{
   lld temp = val;
   while( temp )
   {
      int n = temp%10;
      arr[n] = true;
      temp /= 10;
   }
}

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
   char ee[10];
   T = fscanf( fin, "%s",ee );
   T = atoi(ee);
   printf("%d\n",T);
   for( int x=1;x<=T;x++ )
   {
      llu val=0;
      fscanf(fin,"%s",ee);
      val = atoi(ee);
      bool arr[10]={0};
      int i=0;
      if( 0 != val )
      {
         while( !correctArray( arr ) )
         {
            ++i;
            getDigits( i*val,arr );
         }
         fprintf( fout, "Case #%d: %lld\n",x, i*val );
      }
      else
      {
         fprintf( fout, "Case #%d: INSOMNIA\n",x );
      }
   }
   
   return 0;
}
