#include <cstdio>
#include <iostream>
using namespace std;
int main ()
{
  int t;
  scanf ("%d", &t);
  
  for (int yolo=1; yolo<=t; yolo++)
  {
    long double c, f, x;
    scanf ("%Lf %Lf %Lf", &c, &f, &x);
    
    long double wynik=x;
    long double akt=0.0, zysk=2.0;
   
    for (int i=0; i<=int (x); i++)
    {
      wynik=min (wynik, akt+x/zysk);
      
      akt+=c/zysk;
      zysk+=f;
    }
    
    printf ("Case #%d: %.7Lf\n", yolo, wynik);
  }
    
  return 0;
}