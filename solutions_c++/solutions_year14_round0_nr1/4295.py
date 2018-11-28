
#include <iostream>
#include <string>
#include <sstream>

int main() {
	std::string line;

	int numTestCases = 0;
	std::getline(std::cin, line);
	sscanf(line.c_str(), "%d", &numTestCases);

	for(int testCase = 0; testCase < numTestCases; testCase++) {
    unsigned int cards = 0xFFFF;

    for(int step = 0; step < 2; step++) {
      int chosenRow;

      std::getline(std::cin, line);
      sscanf(line.c_str(), "%d", &chosenRow);
      chosenRow--;

      for(int row = 0; row < 4; row++) {
        int v[4];

        std::getline(std::cin, line);
        sscanf(line.c_str(), "%d %d %d %d", v, v + 1, v + 2, v + 3);

        if(row != chosenRow) {
          for(int card: v) {
            cards &= ~(1 << (card - 1));
          }
        }
      }
    }

    int value = -1;
    for(int i = 0; i < 16; i++) {
      if((cards & (1 << i)) > 0) {
        value = i;
      }
    }

    if(value >= 0) {
      if(cards == (1 << value)) {
        std::cout << "Case #" << (testCase + 1) << ": " << (value + 1) << std::endl;
      } else {
        std::cout << "Case #" << (testCase + 1) << ": Bad magician!" << std::endl;
      }
    } else {
      std::cout << "Case #" << (testCase + 1) << ": Volunteer cheated!" << std::endl;
    }
  }

  return 0;
}
