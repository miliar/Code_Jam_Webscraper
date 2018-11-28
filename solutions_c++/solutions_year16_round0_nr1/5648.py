#include <iostream>
#include <string>
#include <fstream>

std::string count_sheep(int n);

int main(int argc, const char *argv[])
{
  std::ifstream infile(argv[1]);
  int num;
  int n;

  infile >> num;
  for (int i = 0; i < num; i++){
    infile >> n;
    std::cout << "Case #" + std::to_string(i + 1) + ": " + count_sheep(n) << std::endl;
  }

  return 0;
}

std::string count_sheep(int n){
  int last;
  int scalar = 1;
  int seen[10];
  for (int i = 0; i<10; i++) seen[i] = 0;
  int n_seen = 0;

  if (n == 0){
    return "INSOMNIA";
  }

  while (n_seen != 10) {
    int  tmp = n * scalar;

    while (tmp != 0){
      int dig = tmp % 10;
      if (seen[dig] == 0){
        seen[dig] = 1;
        n_seen++;
      }

      tmp /= 10;
    }

    last = n * scalar;
    scalar++;
  }

  return std::to_string(last);
}
