#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<cstdlib>

using namespace std;

void printIntegerArray(std::vector<long> v) {
  //std::cout << "Size: " << n << std::endl;
  for (long val: v) {
    std::cout << val << " ";
  }

  std::cout << std::endl;
}


void read_values(const char *file_name) {
    fstream is;
    is.open(file_name, std::fstream::in);

    char alphabet[26] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };

    long cases(0);
    long caseNo(1);
    is >> cases;

    while (caseNo <= cases) {

        long no_values(0);
        is >> no_values;

        long values[no_values];
        for (size_t i = 0; i < no_values; i++) {
            /* code */
            is >> values[i];
        }

        long maxIdx(0);
        long minIdx(0);
        long midIdx(0);
        for (size_t i = 0; i < no_values; i++) {
          /* code */
          if(values[i] > values[maxIdx]) {
            maxIdx = i;
          }

          if(values[i] < values[maxIdx]) {
            minIdx = i;
          }
        }

        long temp = values[maxIdx];
        values[maxIdx] = 0;

        for (size_t i = 0; i < no_values; i++) {
          /* code */
          if(values[i] > values[midIdx]) {
            midIdx = i;
          }
        }

        values[maxIdx] = temp;
        std::cout << "Case #" << caseNo << ": ";
        long diff = (values[maxIdx] - values[midIdx]);
        while (diff > 0) {
          /* code */
          if(diff >= 2) {
            std::cout << alphabet[maxIdx] << alphabet[maxIdx] << " ";
            values[maxIdx]-=2;
            diff -= 2;
          }
          else if (diff > 0) {
            /* code */
            std::cout << alphabet[maxIdx] << " ";
            values[maxIdx] -= 1;
            diff -= 1;
          }
        }

        for (size_t i = 0; i < no_values; i++) {
          if(i!=maxIdx && i!=midIdx) {
              while (values[i] > 0) {
                if(values[i] >= 2) {
                  std::cout << alphabet[i] << alphabet[i] << " ";
                  values[i]-=2;

                }
                else if (values[i] > 0) {
                  std::cout << alphabet[i] << " ";
                  values[i]-=1;
                }
                else {
                  break;
                }
              }
          }
        }

        while (values[maxIdx] > 0) {
          std::cout << alphabet[maxIdx] << alphabet[midIdx] << " ";
          values[maxIdx]-=1;
        }

        std::cout << std::endl;
        // Carry out the operations here.
        caseNo+=1;
    }

    is.close();
}

int main(int argc, char const *argv[]) {
    read_values(argv[1]);
    return 0;
}
