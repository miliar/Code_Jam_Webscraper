#include <iostream>
#include <stdio.h>
#include <fstream>
#include <vector>
#include <cassert>

void doLine(std::string input, std::ofstream &output);

int main(int argc, char *argv[])
{
  char buffer[300];
  FILE * input = fopen("input.txt", "r");
  if (input == NULL)
    printf("no file scrub");
  else {
    std::ofstream output("output.txt");
    int amount = atoi(fgets(buffer, 100, input));
    while(fgets(buffer, 300, input) != NULL) {
      doLine(std::string(buffer), output);
    }
    fclose(input);
    output.close();
  }

}

bool arrayAnd(bool bools[], int size) {
  for(int i = 0; i < size; i++)
    if(!bools[i])
      return false;
  return true;
}

std::vector<bool> toBoolArray(std::string input) {
  std::vector<bool> v;
  for(int i = 0; i < input.length(); i++) {
    if (input[i] == '+')
      v.push_back(true);
    if (input[i] == '-')
      v.push_back(false);
  }
  return v;
}

std::vector<bool> flip(std::vector<bool> input, int endIndex) {
  assert(endIndex < input.size());
  auto output = input;
  for (int i = 0; i < endIndex; i++)
    output[i] = !input[endIndex-i];
  return output;
}

void doLine(std::string input, std::ofstream &output) {
  static int i = 0;
  int result = 0;
  std::vector<bool> bools = toBoolArray(input);
  bool lastBool = !bools[0];
  for(bool b: bools)
    if(b!=lastBool) {
      lastBool = b;
      result ++;
    }
  if (bools.back())
    result--;

  output << "Case #" << ++i << ": " << result << std::endl;
}
