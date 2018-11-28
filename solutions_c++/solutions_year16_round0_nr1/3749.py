#include <iostream>
#include <fstream>

using namespace std;

int sum(int y[]) {
  int sum = 0;
  for(int i=0; i<10; i++) {
    sum += y[i];
  }
  return sum;
}

int main () {

  ifstream fin("A-large.in");
  ofstream fout("A-large.out");

  int n, t;
  fin>>t;

  for(int i=1; i<=t; i++){

    fin>>n;

    if(n==0){
      fout<<"Case #"<<i<<": INSOMNIA"<<endl;
    } else {
      int retVal = n, k = 1, digit;

      int x[10] = { 0,0,0,0,0,0,0,0,0,0 };

      while(sum(x)!=10) {
        retVal = n * k++;
        while(retVal != 0) {
          x[retVal % 10] = 1;
          retVal /= 10;
        }
      }
      fout<<"Case #"<<i<<": "<<n * --k<<endl;
    }

  }

  fin.close();
  fout.close();
  return 0;
}