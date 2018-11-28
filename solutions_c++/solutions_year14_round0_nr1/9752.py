#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<std::vector<int> > Cards;

struct Arrangement {
  int answer;
  Cards cards;
};

Cards ReadCards() {
  Cards cards;
  const int cardNumber = 4;

  for (int row = 0; row < cardNumber; ++row) {
    std::vector<int> row;
    int current = 0;
    for (int card = 0; card < cardNumber; ++card) {
      std::cin >> current;
      row.push_back(current);
    }
    cards.push_back(row);
  }

  return cards;
}

void Magic(int caseNum, const Arrangement& arr1, const Arrangement& arr2) {
  std::vector<int> first_row = arr1.cards[arr1.answer - 1];
  std::vector<int> second_row = arr2.cards[arr2.answer - 1];
  std::sort(first_row.begin(), first_row.end());
  std::sort(second_row.begin(), second_row.end());
  
  std::vector<int> magic_card(8);
  std::vector<int>::iterator iter = std::set_intersection(
      first_row.begin(), first_row.end(), 
      second_row.begin(), second_row.end(),
      magic_card.begin());
  magic_card.resize(iter - magic_card.begin()); 

  std::cout << "Case #" << caseNum << ": ";
  size_t mcards = magic_card.size();
  if (mcards == 1) {
    std::cout << magic_card[0] << std::endl;
  } else if (mcards > 1) {
    std::cout << "Bad magician!" << std::endl;
  } else {
    std::cout << "Volunteer cheated!" << std::endl;
  }
}

int main(int argc, const char *argv[]) {
  int test_cases = 0;
  std::cin >> test_cases;

  Arrangement arr1, arr2;
  for (int test = 1; test <= test_cases; ++test) {
    std::cin >> arr1.answer;
    arr1.cards = ReadCards();
    std::cin >> arr2.answer;
    arr2.cards = ReadCards();
    Magic(test, arr1, arr2);
  }

  return 0;
}
