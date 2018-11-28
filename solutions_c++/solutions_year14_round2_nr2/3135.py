#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char*argv[]) {
  ifstream file (argv[1]);

  if (file.is_open()) {
    int T, A, B, K, count, max, val;
    file >> T;

    for (int i = 0; i < T; i++) {
      file >> A >> B >> K;
      count = 0;
      max = (A > B) ? (A) : (B);

      if (K > max) {
        count = A*B;
      } else {
        for (int a = 0; a < A; a++) {
          for (int b = 0; b < B; b++) {
            val = a & b;
            if (K > val) {
              count++;
            }
          }
        }
      }

      cout << "Case #" << i+1 << ": " << count << endl;
    }
  }
}
