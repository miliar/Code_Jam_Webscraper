#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

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
    int N;
    input >> N;

    vector<float> Nao(N);
    vector<float> Ken(N);

    for(int i = 0; i < N; i++){
      input >> Nao[i];
    }

    for(int i = 0; i < N; i++){
      input >> Ken[i];
    }

    // compute output
    sort(Nao.begin(), Nao.end());
    sort(Ken.begin(), Ken.end());

    int win1 = 0, win2 = 0;

    // deceitful war score
    int iNao = N-1;
    int iKen = N-1;

    while(iNao >= 0 && iKen >= 0){
      while(iKen >= 0 && Ken[iKen] > Nao[iNao]){
        iKen --;
      }
      if(iKen >= 0){
        win1 ++;
        iNao --;
        iKen --;
      }
    }
    
    iNao = 0;
    iKen = 0;

    while(iNao < N && iKen < N){
      while(iKen < N && Ken[iKen] < Nao[iNao]){
        iKen ++;
      }
      if(iKen < N){
        win2 ++;
        iNao ++;
        iKen ++;
      }
    }

    // optimal war score

    // write output file
    output << "Case #" << k+1 << ": " << win1 << " " << N-win2 << endl;
  }

  return 0;
}