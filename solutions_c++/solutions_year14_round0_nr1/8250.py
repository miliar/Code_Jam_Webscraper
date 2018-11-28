#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

constexpr int ROWS = 4;
constexpr int COLS = 4;

using std::begin;
using std::end;

std::vector<int> parse_arrangement() {
  // read the card's row
  int iCardRow;
  std::cin >> iCardRow;
  --iCardRow;

  // read the card arragement
  std::vector<std::vector<int>> cardRows;
  for (auto iRow = 0; iRow < ROWS; iRow++) {
    std::vector<int> rowCards;
    for (auto iCol = 0; iCol < COLS; iCol++) {
      int card;
      std::cin >> card;
      rowCards.push_back(card);
    }
    cardRows.push_back(std::move(rowCards));
  }

  // get cards in chosen row
  std::vector<int> possibleCards = cardRows[iCardRow];
  std::sort(begin(possibleCards), end(possibleCards));
  return possibleCards;
}

std::string format_result(std::vector<int> solutions) {
  if (solutions.size() == 1)
    return std::to_string(solutions[0]);
  else if (solutions.size() == 0)
    return "Volunteer cheated!";
  else // (solutions.size() > 1)
    return "Bad magician!";
}

int main(int argv, char** argc) {
  int nTestCases;
  std::cin >> nTestCases;

  for (auto i=0; i<nTestCases; ++i) {
    auto firstCards = parse_arrangement();

    auto secondCards = parse_arrangement();

    std::vector<int> solutions;
    std::set_intersection(begin(firstCards), end(firstCards), begin(secondCards),
                          end(secondCards), std::back_inserter(solutions));

    std::cout << "Case #" << (i+1) << ": " << format_result(solutions) << std::endl;
  }
}
