#include <iostream>

using namespace std;

const char * BAD_MAGICIAN = "Bad magician!";
const char * VOLUNTEER_CHEATED = "Volunteer cheated!";

size_t getChosenCard(size_t first_row[4], size_t second_row[4], size_t & result)
{
  size_t number_of_results = 0;
  for (size_t i = 0; i < 16; ++i)
    if (first_row[i/4] == second_row[i%4]) 
    {
      ++number_of_results;
      result = first_row[i/4];
    }
  return number_of_results;
}

int main(int argc, char** argv)
{
  size_t number_of_testcases;
  cin >> number_of_testcases;
  for (size_t tc_number = 1; tc_number <= number_of_testcases; ++tc_number)
  {
    size_t row1;
    size_t row2;
    size_t table1[4][4];
    size_t table2[4][4];
    
    cin >> row1;
    for (size_t i = 0; i < 16; ++i) cin >> table1[i/4][i%4];
    cin >> row2;
    for (size_t i = 0; i < 16; ++i) cin >> table2[i/4][i%4];
    
    cout << "Case #" << tc_number << ": ";
    
    size_t result = 0, num_of_results = getChosenCard(table1[row1-1], table2[row2-1], result);
    
    switch ( num_of_results)
    {
      case 0:
	cout << VOLUNTEER_CHEATED << endl;
	break;
      case 1:
	cout << result << endl;
	break;
      default:
	cout << BAD_MAGICIAN << endl;
	break;
    }
  }
}
