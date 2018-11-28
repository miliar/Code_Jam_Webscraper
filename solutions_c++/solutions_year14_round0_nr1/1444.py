#include <iostream>
#include <set>
#include <string>

int main()
{
  int T;
  int rowNo;
  std::string val;
  std::set<std::string> valuesSelected;

  std::cin >> T;

  // for each case
  for (int i = 1; i <= T; ++i) {

    valuesSelected.clear();
    bool isVolLying = true;
    bool finished = false;
    int noSelected = 0;
    std::string status = "";

    // get row number (first round)
    std::cin >> rowNo;

    // insert first four elements (first round)
    for (int j = 0; j < 16; ++j) {
      std::cin >> val;
      if (j/4 == rowNo-1) {
	valuesSelected.insert(val);
      }
    }

    // get row number (2nd round)
    std::cin >> rowNo;

    for (int j = 0; j < 16; ++j) {

      // get all elements
      std::cin >> val;

      // add to set only the ones for the correct row
      if (j/4 == rowNo-1 && !finished) {
	// if element already exists (return false), volunteer wasn't lying and this number is candidate for final answer
	if(!valuesSelected.insert(val).second) {
	  isVolLying = false;
	  status = val;
	  ++noSelected;
	}

	if (noSelected > 1) {
	  status = "Bad magician!";
	  finished = true;
	}
      }
    }
    if (isVolLying) {
      status = "Volunteer cheated!";
    }

    std::cout << "Case #" << i << ": " << status << std::endl;
  }

  return 0;
}
