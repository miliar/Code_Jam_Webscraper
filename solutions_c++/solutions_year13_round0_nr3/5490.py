#include <stdio.h>
#include <math.h>
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int write(){

    FILE *f;
    f=fopen("C.out","w");
    if(f==NULL){return 0;}

        fprintf(f,"%d %d %d\n", 1, 2, 3);

    return 1;
}

int read(){
    int i;
    FILE *f;
    f=fopen("C.in","r");
    if(f==NULL){return 0;}

//        fscanf(f,"%s %s %d %d %d", &array[i].name, &array[i].address,
//               &array[i].phone, &array[i].numb_facult, &array[i].numb_stud);

    return 1;
// fgetc(f);
}

bool checkPolindrom(int numb) {
  int dig, rev, n;
  n = numb;
  rev = 0;
  while (numb > 0)
  {
      dig = numb % 10;
      rev = rev * 10 + dig;
      numb = numb / 10;
  }

  if (n == rev) {
      return true;
  } else {
      return false;
  }

}

bool checSquare(int numb) {
    double d_sqrt = sqrt( numb );
    int i_sqrt = d_sqrt;
    if ( d_sqrt == i_sqrt )
        // Your number is a perfect square
    {
        return true;
    }
        return false;
}


int main() {
  int nrGames, A, B, counter = 0;
  FILE *f, *f2;
  f=fopen("C.in","r");
  f2=fopen("C.out","w");
  if(f==NULL){return 0;}
  fscanf(f, "%d", &nrGames);
  fgetc(f);

  for(int i = 1; i <= nrGames; i++) {
    fscanf(f, "%d %d", &A, &B);

    counter = 0;
    for(int j = A; j <= B; j++) {
      if(checkPolindrom(j) && checSquare(j)) {
        if(checkPolindrom(sqrt(j))) {
          counter++;
        }
      }
    }
    fprintf(f2,"Case #%d: %d\n", i, counter);

  }

return 0;
}
