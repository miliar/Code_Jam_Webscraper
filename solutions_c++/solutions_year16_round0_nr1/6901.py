#include <iostream>
#include <fstream>

// Function prototypes
void digitsSeen(uint num, uint &digits);
void printDigitsSeen(const uint digits);

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
  int T,N,C;
  // set each bit to 1 if digit seen
  // check against 0x3FF
  uint digits = 0;
  // temp string to read to
  std::string tempString;

  std::getline(fin, tempString);
  T = std::stoi(tempString);

  std::cout << T << " test cases following\n";

  for (int i = 0; i < T; i++){
    // reset each time!
    digits = 0;
    C = 0;
    std::getline(fin, tempString);
    N = std::stoi(tempString);
    std::cout << "Case " << i << ": N is " << N << std::endl;
    if (N != 0){
      while((digits & 0x3FF) != 0x3FF){
        C++;
        digitsSeen(C*N, digits);
      }
    }

    fout << "Case #" << i + 1 << ": ";
    (C!=0)? fout << C*N : fout << "INSOMNIA";
    fout << std::endl;



  }

  // Cleanup
  fin.close();
  fout.close();

  return 0;
}

void digitsSeen(uint num, uint &digits){
  while(true){
    if (num < 10){
      digits |= (1 << num);
      break;
    }else{
      digits |= (1 << (num % 10));
      num /= 10;
    }
  }
}

void printDigitsSeen(const uint digits){
  for (int i = 0; i < 10; i++){
    if (digits & (1 << i)){
      std::cout << i << "    seen" << std::endl;
    }else{
      std::cout << i << "not seen" << std::endl;
    }
  }
}
