#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> readQuestion() {
  int row;
  std::vector<int> cards(4);
  std::cin >> row;
  row -= 1;

  int ignore;
  for(int i=0; i<row; ++i) 
    for(int j=0; j<4; ++j) 
      std::cin >> ignore;
  std::cin >> cards[0] >> cards[1] >> cards[2] >> cards[3];
  for(int i=row+1; i<4; ++i) 
    for(int j=0; j<4; ++j) 
      std::cin >> ignore;
  return cards;
}

int main() {
  int testCases;
  std::cin >> testCases;

  for(int tc=1; tc<=testCases; ++tc) {
    std::vector<int> firstCards = readQuestion();
    std::vector<int> secondCards = readQuestion();
    std::vector<int> i(4);
    std::sort(std::begin(firstCards), std::end(firstCards));
    std::sort(std::begin(secondCards), std::end(secondCards));
    auto it = std::set_intersection(std::begin(firstCards), std::end(firstCards), std::begin(secondCards), std::end(secondCards), std::begin(i));
    i.resize(it-std::begin(i));
    std::cout << "Case #" << tc << ": ";
    if(i.size() == 1)
      std::cout << i[0] << "\n";
    else if(i.size() > 1)
      std::cout << "Bad magician!\n";
    else
      std::cout << "Volunteer cheated!\n";
  }
  
  return 0;
}
