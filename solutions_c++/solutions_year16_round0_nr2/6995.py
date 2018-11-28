#include <iostream>
#include <fstream>

// Function prototypes
int numSignChanges(std::string S);

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

  // Number of tests
  int T;
  // input string
  std::string S;
  std::string tempString;

  std::getline(fin, tempString);
  T = std::stoi(tempString);

  std::cout << T << " test cases following\n";

  for (int i = 0; i < T; i++){
    std::getline(fin, S);
    std::cout << "Case " << i << ": S is " << S << std::endl;
    fout << "Case #" << i + 1 << ": ";
    fout << numSignChanges(S);
    fout << std::endl;
  }

  // Cleanup
  fin.close();
  fout.close();

  return 0;
}

int numSignChanges(std::string S){
  int signChanges = 0;
  S += '+';
  char previousChar = S.at(0);
  for (int i = 1; i < S.length(); i++){
    if (previousChar != S.at(i)){
      signChanges++;
    }
    previousChar = S.at(i);
  }

  return signChanges;
}
