#include<iostream>
#include<fstream>
#include<cmath>
#include<algorithm>

void printIntegerArray(long *a, int n) {
  //std::cout << "Size: " << n << std::endl;
  for (size_t i = 0; i < n; i++) {
    std::cout << a[i] << " ";
  }
  std::cout << std::endl;
}



void writeTheLetters(char *letters, long start, long end, long caseNo) {
  /* code */
  char writter[1000];
  for (size_t i = 0; i <= end; i++) {
    /* code */

    if(letters[i] == '\n' || letters[i] == '\t' || strlen(&letters[i]) == 0 || letters[i] == ' ' || letters[i] == '\0') {
        break;
    }

    if(i == 0) {
      writter[0] = letters[0];
    }
    else if(letters[i] < writter[0]) {
      writter[i] = letters[i];
    }
    else if (letters[i] >= writter[0]) {
      for (size_t j=(i); j > 0; j--) {
        /* code */
        writter[j] = writter[j-1];
      }
      writter[0] = letters[i];
    }
    else {
      writter[i] = letters[i];
    }
  }

  std::cout << "Case #" << caseNo << ": ";
  for (int i = 0; i <= end; i++) {
    std::cout << writter[i];
  }
  std::cout << std::endl;
}

void solve (const char *fileName) {
  std::ifstream iStream;
  iStream.open(fileName);

  long numberOfCases(0);
  iStream >> numberOfCases;
  std::cout << "Total number of cases: " << numberOfCases << std::endl;


  long caseNo(1);
  while (caseNo <= numberOfCases) {
    /* code */
    std::string line;
    iStream >> line;

    char b[sizeof(line)];
    int j = 0;
    for (int i = 0; i < sizeof(line); i++) {
      if(line[i] == '\n' || line[i] == '\t' || strlen(&line[i]) == 0 || line[i] == ' ' || line[i] == '\0') {
          break;
      }

      b[j] = line[i];
      j++;
    }

    writeTheLetters(b, 0, j-1, caseNo);
    caseNo+=1;
  }
  //printIntegerArray(array, numberOfBarbers);
}

int main(int argc, char const *argv[]) {
  std::cout << "Number of arguments: " << argc << std::endl;

  if(argc > 1) {
    std::cout << "File Name: " << argv[1] << std::endl;
    solve(argv[1]);
  }

  return 0;
}
