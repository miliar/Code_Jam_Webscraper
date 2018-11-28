#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <utility>

std::vector<int> find_card(int first_answer, std::vector<std::vector<int> > first_deck,
                           int second_answer, std::vector<std::vector<int> > second_deck)
{
  std::vector<int> first_row;
  first_row = first_deck.at(first_answer-1);
  std::vector<int> second_row;
  second_row = second_deck.at(second_answer-1);

  std::vector<int> result;
  for(std::vector<int>::iterator it = first_row.begin(); 
      it != first_row.end(); 
      ++it) {
    for(std::vector<int>::iterator itt = second_row.begin();
        itt != second_row.end();
        ++itt) {
      if(*it == *itt) {
        result.push_back(*it);
      }
    }
  }
  return result;
}

int main()
{
  std::string filename = "testFile";
  std::ifstream file(filename.c_str());
  int numCases;

  file >> numCases;

  for(int i = 0; i < numCases; ++i) {
    int first_answer;
    file >> first_answer;
    std::vector<std::vector<int> > first_deck;
    for(int j = 0; j < 4; ++j) {
      std::vector<int> tmp_vec;
      for(int k = 0; k < 4; ++k) {
        int tmp;
        file >> tmp;
        tmp_vec.push_back(tmp);
      }
      first_deck.push_back(tmp_vec);
    }

    int second_answer;
    file >> second_answer;
    std::vector<std::vector<int> > second_deck;
    for(int j = 0; j < 4; ++j) {
      std::vector<int> tmp_vec;
      for(int k = 0; k < 4; ++k) {
        int tmp;
        file >> tmp;
        tmp_vec.push_back(tmp);
      }
      second_deck.push_back(tmp_vec);
    }

    std::vector<int> result;
    result = find_card(first_answer, first_deck, second_answer, second_deck);


    // for(std::vector<int>::iterator it = result.begin();
    //     it != result.end();
    //     ++it) {
    //   std::cout << *it << " ";
    // }
    // std::cout << std::endl;



    std::cout << "Case #" << i+1 << ": ";
    if (result.size() == 1) {
      std::cout << result.at(0)  << std::endl;
    } else if (result.size() == 0 ) {
      std::cout << "Volunteer cheated!" << std::endl;
    } else {
      std::cout << "Bad magician!" << std::endl;
    }
  }
}
