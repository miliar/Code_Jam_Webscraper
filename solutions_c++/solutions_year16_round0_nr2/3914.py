#include <iostream>
#include <sstream>

std::string ultos(unsigned long long number) {
  std::ostringstream strs;
  strs << number;
  return strs.str(); 
} 

void flip(bool* arr, unsigned int len, unsigned int idx) {
  for (int i = 0 ; i <= idx && i < len; i++) {
    arr[i] = !arr[i];
  }
}

// return -1 if no unhappy cakes
int lastUnhappy(bool* arr, unsigned int len) {
  int idx = -1;
  for (int i = 0; i < len; i++) {
    if (!arr[i])
      idx = i;
  }
  return idx;
}

int main(int argc, char** argv) {
  unsigned long long MAX_LEN = 100;
  unsigned int T;
  std::cin >> T;

  for (int i = 0; i < T; i ++) {
    std::string S;
    std::cin >> S;

    unsigned int len = S.size();
    bool cakes[len];
    bool done = false;
    int num_flips = 0;

    unsigned int j = 0;
    for (std::string::size_type k = 0; k < len; k++) {
      if (S[k] == '-')
        cakes[j] = false;
      else
        cakes[j] = true;
      j++;
    }

    // special case, already alll happy
    if (lastUnhappy(cakes, len) == -1)
      done = true;

    while (!done) {
      // flip all up to last unhappy cake (greedy)
      int last_unhappy_idx = lastUnhappy(cakes, len);
      if (last_unhappy_idx != -1) {
        flip(cakes, len, last_unhappy_idx);
        num_flips++;
      }
      else {
        done = true;
      }
    }

    // output
    std::cout << "Case #" << i+1 << ": " << num_flips << std::endl;
  }

  return 0;
}

