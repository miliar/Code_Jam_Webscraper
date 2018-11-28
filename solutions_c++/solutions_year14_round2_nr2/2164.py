#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <cmath>
using namespace std;

long long g(int A,int B,int K){
    long long ctr = 0;
    for(int i = 0;i < A;i++)
        for(int j = 0;j < B;j++){
            long long temp = i&j;
            if(temp < K)
                ctr++;
        }
    return ctr;
}
int main(){
  ofstream fout ("output.out");
  ifstream fin ("B-small-attempt0.in");
  int T,A,B,K;
  fin >> T;
  for(int i = 1;i <= T;i++){
      fin >> A >> B >> K;
      fout << "Case #" << i << ": " << g(A,B,K) << "\n";
  }
  return 0;
}