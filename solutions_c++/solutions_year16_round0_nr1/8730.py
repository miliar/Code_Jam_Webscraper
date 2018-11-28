#include <iostream>
#include <stdio.h>
#include <fstream>

void doLine(int input, std::ofstream &output);
int amounts(int input);

int main(int argc, char *argv[])
{
  char buffer[100];
  FILE * input = fopen("input.txt", "r");
  if (input == NULL)
    printf("no file scrub");
  else {
    std::ofstream output("output.txt");
    int amount = atoi(fgets(buffer, 100, input));
    while(fgets(buffer, 100, input) != NULL) {
      doLine(atoi(buffer), output);
    }
    fclose(input);
    output.close();
  }

}

void doLine(int input, std::ofstream &output) {
  static int i = 0;
  std::string result = "";
  if (input != 0) {
    result = std::to_string(amounts(input));
  } else
    result = "INSOMNIA";
  output << "Case #" << ++i << ": " << result << std::endl;
}

bool arrayAnd(bool bools[], int size) {
  for(int i = 0; i < size; i++)
    if(!bools[i])
      return false;
  return true;
}

int amounts(int input) {
  int i = 0;
  bool digits[10] = {false};
  while (!arrayAnd(digits, 10)) {
    i++;
    std::string curr = std::to_string(i*input);
    for(int j = 0; j < 10; j++) {
      if (curr.find(std::to_string(j)) != -1)
        digits[j] = true;
    }
  }
  return i*input;
}
