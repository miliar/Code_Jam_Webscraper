#include <iostream>
#include <algorithm>
#define ll long long int
#include <fstream>
using namespace std;
ifstream in("input.in");
ofstream out("output.out");
short int pos(char s)
{
    if(s == '1')
        return 0;
    if(s == 'i')
        return 1;
    if(s == 'j')
        return 2;
    if(s == 'k')
        return 3;
}
int main()
{
  char quat[4][4] = {{'1','i','j','k'},{'i','1','k','j'},{'j','k','1','i'},{'k','j','i','1'}};
  short int semn[4][4]={{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};
  char sir[10003];
  int L,X,i,j,T,s,jg; bool fi,se,th;
  char caracter;
  in >> T;
  for( i = 1 ; i <= T ; i++)
  {
      out <<"Case #"<<i<<": ";
      fi = se = th = false;
      s = 1;
      in >> L >> X;
      in >> sir;
      j = 0;
      jg = 0;
      caracter = '1';
      while(jg<X)
      {
        if (s == 1 && caracter == 'i')
         {
            fi = true;
            break;
         }
         if(j == L)
         {
             j = 0;
             jg++;
         }
         else
         {
             s *=semn[pos(caracter)][pos(sir[j])];
             caracter = quat[pos(caracter)][pos(sir[j])];
             j++;
         }
      }
      caracter = '1';
      while(jg<X)
      {
         if (s == 1 && caracter == 'j')
         {
              se = true;
              break;
         }
         if(j == L)
         {
             j = 0;
             jg++;
         }
         else
         {
             s *=semn[pos(caracter)][pos(sir[j])];
             caracter = quat[pos(caracter)][pos(sir[j])];
             j++;
         }
      }
      caracter = '1';
      while(jg<X)
      {
         if(j == L)
         {
             j = 0;
             jg++;
         }
         else
         {
             s *=semn[pos(caracter)][pos(sir[j])];
             caracter = quat[pos(caracter)][pos(sir[j])];
             j++;
         }
      }
      if (s == 1 && caracter == 'k')
           th = true;
      if( fi && se && th)
          out<<"YES\n";
      else
          out<<"NO\n";
  }

    return 0;
}
