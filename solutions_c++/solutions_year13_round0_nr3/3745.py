#include <cstdio>
#include <iostream>
#include <vector>
#include <sstream> 
#include <string>
using namespace std;
typedef int typ;

bool napierdalaj (typ liczba){
  stringstream ss;
  ss << liczba;
  string str = ss.str();
  int l,p;
  l = 0;
  p = str.length()-1;
  while (l < p){
    if (str[l] != str[p])
      return false;
    l ++;
    p --;
  }
  return true;
}

int main(){
  typ t, T, l, p, i, j, wynik, ld, pd, m, n, zdr;

  scanf ("%d", &T);
  for (t = 1; t <= T; t++){
    wynik = 0;
    scanf ("%d %d", &l, &p);
    if (l == 1)
      ld = 1;
    else {
      m = l;
      n = 1;
      while(m > n){
        zdr = (m+n)/2;
        if (zdr*zdr <l)
          n = zdr+1;
        else
          m = zdr;
        
      }
      ld = m;
      
    }
    //printf ("%d %d %d\n", t, ld, l);
    while(ld*ld <= p){
      
  
      if ((napierdalaj(ld)) && (napierdalaj(ld*ld)))
        wynik ++;
        
      ld ++;
    }
    printf ("Case #%d: %d\n", t, wynik);
    
  }
  
  return 0;
}
