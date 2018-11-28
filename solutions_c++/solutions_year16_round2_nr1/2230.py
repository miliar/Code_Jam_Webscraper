#include <iostream>
#include <fstream>

// Function prototypes


int main(int argc, const char * argv[]){
  // Check flags
  if (argc<3){
    std::cout << "INPUT AND OUTPUT FLAGS REQUIRED!" << std::endl;
    exit(EXIT_FAILURE);
  }

  // Open in and out files
  std::ifstream fin(argv[1]);
  if(!fin.is_open()) {
    std::cout << "Unable to open input file: " << argv[1] << std::endl;
    exit(EXIT_FAILURE);
  }
  std::ofstream fout(argv[2]);

  // T tests of single integer N
  // C is number of times needed
  int T;

  // temp string to read to
  std::string tempString, s;

  std::getline(fin, tempString);
  T = std::stoi(tempString);

  std::cout << T << " test cases following\n";

  int nZ, nW, nH, nU, nX, nG, nF, nV, nO, nI;
  int digits[10];

  for (int i = 0; i < T; i++){
    // reset
    nZ = 0; nW = 0; nH = 0; nU = 0; nX = 0; nG = 0; nF = 0; nV = 0; nO = 0, nI = 0;
    for (int j = 0; j <10; j++){
      digits[j] = 0;
    }

    // do stuff
    std::getline(fin, s);
    std::cout<<s<<std::endl;

    for (int j = 0; j<s.length(); j++){
      if (s[j] == 'Z') nZ++;
      if (s[j] == 'W') nW++;
      if (s[j] == 'H') nH++;
      if (s[j] == 'U') nU++;
      if (s[j] == 'X') nX++;
      if (s[j] == 'G') nG++;
      if (s[j] == 'F') nF++;
      if (s[j] == 'V') nV++;
      if (s[j] == 'O') nO++;
      if (s[j] == 'I') nI++;
    }

    std::cout<<nZ<<nW<<nH<<nU<<nX<<nG<<std::endl;

    digits[0] = nZ;
    digits[2] = nW;
    digits[4] = nU;
    digits[6] = nX;
    digits[8] = nG;
    digits[3] = nH - digits[8];
    digits[5] = nF - nU;
    digits[7] = nV - digits[5];
    digits[1] = nO - digits[0] - digits[2] - digits[4];
    digits[9] = nI - digits[5] - digits[6] - digits[8];



    fout << "Case #" << i + 1 << ": ";
    // write result
    for (int j = 0; j <10; j++){
      std::cout<<digits[j];
      if (digits[j] != 0){
        for(int jj = 0; jj < digits[j]; jj++){
           fout<<j;
        }
      }
    }
    std::cout << std::endl;
    fout << std::endl;



  }

  // Cleanup
  fin.close();
  fout.close();

  return 0;
}
