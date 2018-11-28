#include <iostream>
#include <iomanip>   
#include <fstream>
#include <vector>

using namespace std;

int PGCD(int a, int b){
    while(b!=0){
        int c=a%b;
        a=b;
        b=c;
    }
    return a;
}

float log2(float p){
  int k = 0;
  while(p == floor(p) && p != 1){
    p /= 2.f;
    k ++;
  }
  if(p ==1){
    return k;
  }
  return -1;
}

int main(int argc, char *argv[]) {
  string inPath = argv[1];
  string outPath = argv[2];

  // open two files
  ifstream input(inPath, std::ifstream::in);
  ofstream output(outPath, std::ios::out | std::ios::trunc);

  // read input file
  int nInput;
  input >> nInput;

  for(unsigned int k = 0; k < nInput; k++){
    // read input
    float P, Q;
    char d;
    input >> P >> d >> Q;

    // simplify fraction
    float pgcd = PGCD(P, Q);
    P /= pgcd;
    Q /= pgcd;
    int generation = log2(Q);
    //cout << pgcd << "/" << generation << "/" << P  << "/" << Q << endl;
    if(generation == -1){
      output << "Case #" << k+1 << ": impossible" << endl;
      continue;
    }


    int i = -1;
    float diff = P - 1;
    float pow2 = 1;
    do{
      i ++;
      pow2 *= 2;
      diff = P - pow2;
    } while(diff >0);

    // write output file
    output << "Case #" << k+1 << ": " << generation - i << endl;
  }

  return 0;
}