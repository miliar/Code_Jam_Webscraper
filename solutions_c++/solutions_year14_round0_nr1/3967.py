#include <iostream>
#include <string>
#include <array>

typedef std::array<std::array<int, 4>, 4> Card_layout;

std::string solve(const Card_layout& cards_0,
                  const int row_0,
                  const Card_layout& cards_1,
                  const int row_1)
{
  int last_candidate_card = -1;
  int num_candidate_cards = 0;
  
  // no need for more sophisticated algorithms because there are only
  // 4 cards per row anyway
  for ( int i = 0; i < 4; ++i ) {
    for ( int j = 0; j < 4; ++j ) {
      if ( cards_0[row_0][i] == cards_1[row_1][j] ) {
        last_candidate_card = cards_0[row_0][i];
        ++num_candidate_cards;
      }
    }
  }
  
  if ( num_candidate_cards == 0 ) {
    return "Volunteer cheated!";
  }
  
  if ( num_candidate_cards > 1 ) {
    return "Bad magician!";
  }

  return std::to_string(last_candidate_card);
}

int main() {
  using std::cin;
  using std::cout;
  using std::string;
  
  int num_tests;
  cin >> num_tests;
  
  for ( int t = 1; t <= num_tests; ++t ) {
    
    // read first layout
    int row_0;
    cin >> row_0;
    --row_0;
    Card_layout cards_0;
    for ( int i = 0; i < 4; ++i ) {
      for ( int j = 0; j < 4; ++j ) {
        cin >> cards_0[i][j];
      }
    }

    // read second layout
    int row_1;
    cin >> row_1;
    --row_1;
    Card_layout cards_1;
    for ( int i = 0; i < 4; ++i ) {
      for ( int j = 0; j < 4; ++j ) {
        cin >> cards_1[i][j];
      }
    }

    // output solution
    string solution = solve(cards_0, row_0, cards_1, row_1);
    cout << "Case #" << t << ": " << solution << "\n";
  }
}
