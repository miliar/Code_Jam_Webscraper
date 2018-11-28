#include <iostream>
#include <fstream>
using namespace std;

void perform (int case_num, ofstream & out)
{
  
  out << "Case #" << case_num << ": ";
  int array1[4][4];
  int answer1;
  cin >> answer1;
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      cin >> array1[i][j];
  int array2[4][4];
  int answer2;
  cin >> answer2;
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      cin >> array2[i][j];
  
  int num_cards_found = 0;
  int card_found;
 
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      if (array1[answer1-1][i] == array2[answer2-1][j]) {
	num_cards_found++;
	card_found = array1[answer1-1][i];
      }
    }
  }
  if (num_cards_found == 1)
    out << card_found << endl;
  else if (num_cards_found == 0)
    out << "Volunteer cheated!" << endl;
  else
    out << "Bad magician!" << endl;
}

int main () 
{
  int cases;
  cin >> cases;
  ofstream out ("output.txt");
  int loop_count = 1;
  while (loop_count <= cases) {
    perform (loop_count, out);
    loop_count++;
  }

  return 0;
}
