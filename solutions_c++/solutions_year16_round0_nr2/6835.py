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

lld scanint();

inline lld scanint( )
{
   lld c = getchar_unlocked(),x=0;
   x = 0;
   int neg = 0;
   for(;((c<48 || c>57) && c != '-');c = getchar_unlocked());
   if(c=='-') {neg=1;c=getchar_unlocked();}
   for(;c>47 && c<58;c = getchar_unlocked()) {x = (x<<1) + (x<<3) + c - 48;}
   if(neg) x=-x;
   return x;
}

int n=0;

bool correctString( int count, short a[] )
{
   for( int i=0; i<n; i++ )
   {
      if( 0 == a[i] )
      {
         return false;
      }
   }
   return true;
}

void flip( int count, short *a )
{
   for( int i=count; i<n; i++ )
   {
      if( 0 == a[i] )
      {
         a[i] = 1;
      }
      else if( 1 == a[i] )
      {
         a[i] = 0;
      }
   }
}

int main()
{
   FILE *fp,*fin;
   fp = fopen( "output.txt", "w" );
   if( NULL == fp )
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
   T = fscanf( fin, "%d",&T );
   T = 100;
   for( int x=1;x<=T;x++ )
   {
      char s[101]={0};
      short a[101]={0};
      fscanf(fin,"%s",s);
      printf("%s\n",s);
      n =  strlen(s);
      for( int i=n-1,j=0; i>=0; i--,j++ )
      {
         if( s[i] == '+' )
         {
            a[j] = 1;
         }
         else
         {
            a[j] = 0;
         }
      }
      
      int count = 0;
      while( !correctString(count,a) )
      {
         ++count;
         int pos = 0;
         while( 0 != a[pos] )
         {
            pos++;
         }
         for( int j=pos; j<n; j++ )
         {
            if( 0 == a[j] )
            {
               a[j] = 1;
            }
            else if( 1 == a[j] )
            {
               a[j] = 0;
            }
         }
      }
      fprintf(fp, "Case #%d: %d\n",x, count );
   }

   return 0;
}
