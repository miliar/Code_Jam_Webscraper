#include <algorithm>
#include <array>
#include <cstddef>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>


int main(int /* argc */, const char** argv) {
  std::ifstream ifs(argv[1]);

  unsigned int numberOfTestCases;
  ifs >> numberOfTestCases;
  //std::clog << "numberOfTestCases " << numberOfTestCases << '\n';

  unsigned int rowOfCardInFirstArrangement, rowOfCardInSecondArrangement;
  std::array<std::array<unsigned int, 4>, 4> firstArrangement, secondArrangement;

  for(unsigned int testCase{0}; testCase < numberOfTestCases; ++testCase) {
    ifs >> rowOfCardInFirstArrangement;
    //std::clog << "rowOfCardInFirstArrangement " << rowOfCardInFirstArrangement << "\n\n";

    ifs >> firstArrangement[0][0] >> firstArrangement[0][1] >> firstArrangement[0][2] >> firstArrangement[0][3]
        >> firstArrangement[1][0] >> firstArrangement[1][1] >> firstArrangement[1][2] >> firstArrangement[1][3]
        >> firstArrangement[2][0] >> firstArrangement[2][1] >> firstArrangement[2][2] >> firstArrangement[2][3]
        >> firstArrangement[3][0] >> firstArrangement[3][1] >> firstArrangement[3][2] >> firstArrangement[3][3];

    //std::clog << firstArrangement[0][0] << ' ' << firstArrangement[0][1] << ' ' << firstArrangement[0][2] << ' ' << firstArrangement[0][3] << '\n'
    //          << firstArrangement[1][0] << ' ' << firstArrangement[1][1] << ' ' << firstArrangement[1][2] << ' ' << firstArrangement[1][3] << '\n'
    //          << firstArrangement[2][0] << ' ' << firstArrangement[2][1] << ' ' << firstArrangement[2][2] << ' ' << firstArrangement[2][3] << '\n'
    //          << firstArrangement[3][0] << ' ' << firstArrangement[3][1] << ' ' << firstArrangement[3][2] << ' ' << firstArrangement[3][3] << "\n\n";

    std::array<unsigned int, 4> firstArrangementSelectedRow = firstArrangement[rowOfCardInFirstArrangement - 1];
    std::sort(std::begin(firstArrangementSelectedRow), std::end(firstArrangementSelectedRow));

    //std::clog << firstArrangementSelectedRow[0] << ' ' << firstArrangementSelectedRow[1] << ' ' << firstArrangementSelectedRow[2] << ' ' << firstArrangementSelectedRow[3] << '\n';

    ifs >> rowOfCardInSecondArrangement;
    //std::clog << "rowOfCardInSecondArrangement " << rowOfCardInSecondArrangement << "\n\n";

    ifs >> secondArrangement[0][0] >> secondArrangement[0][1] >> secondArrangement[0][2] >> secondArrangement[0][3]
        >> secondArrangement[1][0] >> secondArrangement[1][1] >> secondArrangement[1][2] >> secondArrangement[1][3]
        >> secondArrangement[2][0] >> secondArrangement[2][1] >> secondArrangement[2][2] >> secondArrangement[2][3]
        >> secondArrangement[3][0] >> secondArrangement[3][1] >> secondArrangement[3][2] >> secondArrangement[3][3];

    std::array<unsigned int, 4> secondArrangementSelectedRow = secondArrangement[rowOfCardInSecondArrangement - 1];
    std::sort(std::begin(secondArrangementSelectedRow), std::end(secondArrangementSelectedRow));

    //std::clog << secondArrangementSelectedRow[0] << ' ' << secondArrangementSelectedRow[1] << ' ' << secondArrangementSelectedRow[2] << ' ' << secondArrangementSelectedRow[3] << '\n';

    std::vector<unsigned int> setIntersection;
    std::set_intersection(
        std::begin(firstArrangementSelectedRow), std::end(firstArrangementSelectedRow),
        std::begin(secondArrangementSelectedRow), std::end(secondArrangementSelectedRow),
        std::back_inserter(setIntersection));

    std::cout << "Case #" << testCase + 1 << ": ";
    const std::size_t setIntersectionSize{setIntersection.size()};
    std::stringstream testResult;
    if(setIntersectionSize == 0) {
      testResult << "Volunteer cheated!";
    }
    else if(setIntersectionSize == 1) {
      testResult << setIntersection.front();
    }
    else {
      testResult << "Bad magician!";
    }
    std::cout << testResult.str() << '\n';
  }

}
