/*
*      Tobias Lønnerød Madsen - m@dsen.tv - tobbentm.com
*/  
#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main(){
  int cases;
  ifstream in("A-large.in");
  ofstream out("A-result-large.out");
  in >> cases;

  for(int i = 1; i <= cases; i++){
    int max; char *big;
    int *pop;

    in >> max; in.ignore();
    pop = new int[max+1];
    big = new char[max+2];

    in.getline(big, max+2);

    for(int j = 0; j <= max; j++){
      pop[j] = big[j]-'0';
    }

    int extra = 0, cur = pop[0];

    for(int j = 1; j <= max; j++){
      if(pop[j] && j > cur+extra){
        extra += j-(cur+extra);
      }
      cur += pop[j];
    }

    out << "Case #" << i << ": " << extra << endl;
  }

  return 0;
}