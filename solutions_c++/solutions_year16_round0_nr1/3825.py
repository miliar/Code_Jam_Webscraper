#include <iostream>
#include <sstream>

std::string ultos(unsigned long long number) {
  std::ostringstream strs;
  strs << number;
  return strs.str(); 
} 

int main(int argc, char** argv) {
  unsigned long long MAX_N = 1000000;
  unsigned int T;
  std::cin >> T;

  for (int i = 0; i < T; i ++) {
    unsigned long long N;
    bool seen[10];
    bool done = false;
    for (int j = 0; j < 10; j++) {
      seen[j] = false;
    }

    std::cin >> N;

    // special case
    if (N == 0) {
      N = MAX_N+1;
    }

    int j;
    for (j = 1; N <= MAX_N && !done; j++) {
      std::string N_str = ultos(N * j);
      for (std::string::size_type k = 0; k < N_str.size(); k++) {
        if (N_str[k] == '0')
          seen[0] = true;
        else if (N_str[k] == '1')
          seen[1] = true;
        else if (N_str[k] == '2')
          seen[2] = true;
        else if (N_str[k] == '3')
          seen[3] = true;
        else if (N_str[k] == '4')
          seen[4] = true;
        else if (N_str[k] == '5')
          seen[5] = true;
        else if (N_str[k] == '6')
          seen[6] = true;
        else if (N_str[k] == '7')
          seen[7] = true;
        else if (N_str[k] == '8')
          seen[8] = true;
        else if (N_str[k] == '9')
          seen[9] = true;
      }

      // check if done
      done = true;
      for (int k = 0; k < 10; k++) {
        done = done && seen[k];
      }
    }
    
    // output
    std::cout << "Case #" << i+1 << ": ";
    if (done) {
      j = j - 1;
      std::cout << j * N << std::endl;
    }
    else {
      std::cout << "INSOMNIA" << std::endl;
    }
  }

  return 0;
}

