#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <string>

void GetParams(std::string &in, const int n_params, std::vector<int> &params) {
  char *ptr = strdup(in.c_str());
  for (int i = 0; i < n_params; i++) {
    if (i == 0) {
      ptr = strtok(ptr, " ");
      params.push_back(atoi(ptr));
    }
    else {
      ptr = strtok(NULL, " ");
      params.push_back(atoi(ptr));
    }
  }
  return;
}

bool AllZero(std::vector<int> &params) {
  for (int i = 0; i < params.size(); i++) {
    if (params[i] != 0) return false;
  }
  return true;
}

void SolveA(std::vector<int> &params) {
  while (!AllZero(params)) {
    int max_pos = -1;
    int max = 0;
    for (int i = 0; i < params.size(); i++) {
      if (max < params[i]) {
        max = params[i];
        max_pos = i;
      }
    }
    if (max_pos != -1) {      
      std::cout << (char)((int)'A' + max_pos);
      params[max_pos]--;
    }
    max_pos = -1;
    max = 0;
    int tot = 0;
    for (int i = 0; i < params.size(); i++) {
      if (max < params[i]) {
        max = params[i];
        max_pos = i;
      }
    }
    if (max_pos != -1) {
      int n_same = 0;
      for (int i = 0; i < params.size(); i++) {
        if (params[i] == max) n_same++;
      }
      if (n_same != 2) {
        std::cout << (char)((int)'A' + max_pos);
        params[max_pos]--;
      }
    }
    std::cout << " ";
  }
  std::cout << std::endl;
}

void GcjA() {
  std::string in_line;
  std::getline(std::cin, in_line);
  const int n_cases = atoi(in_line.c_str());
  for (int i = 0; i < n_cases; i++) {
    std::getline(std::cin, in_line);
    const int n_parties = atoi(in_line.c_str());
    std::vector<int> params;
    std::getline(std::cin, in_line);
    GetParams(in_line, n_parties, params);
    std::cout << "Case #" << i + 1 << ": ";
    SolveA(params);
  }
}

int main() {
  GcjA();
}