#include <fstream>
#include <iostream>
using namespace std;

int main(){

  fstream file;

  int num_cases;
  int row_selected;
  int** cards = new int*[4];
  int * row_values = new int[4];

  for(int i = 0 ; i < 4 ; i ++)
    cards[i] = new int[4];

  file.open("input.dat");

  file >> num_cases;

  for(int i = 0 ; i < num_cases ; i ++){

    for(int s = 0 ; s < 2 ; s ++){
      file >> row_selected;

      for(int j = 0 ; j < 16 ; j ++){
        int t;
        file >> t;
        cards[j / 4][j % 4] = t;
      }

      if(s == 0){ // First read
        for(int j = 0 ; j < 4 ; j ++)
          row_values[j] = cards[row_selected - 1][j];
      }else{ // Second read

        int num_seen = 0;
        int found;
        for(int prev = 0 ; prev < 4 ; prev ++){  // Check each row selected to ensure no duplicate
          for(int k = 0 ; k < 4 ; k ++){
            if(row_values[prev] == cards[row_selected - 1][k]){
              num_seen ++;
              found = row_values[prev];
            }
          }
        }

        switch(num_seen){
          case 0:
            cout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
            break;
          case 1:
            cout << "Case #" << i + 1 << ": " << found << endl;
            break;
          default:
            cout << "Case #" << i + 1 << ": Bad magician!" << endl;
            break;
        }

      }

    }

  }


  for(int i = 0 ; i < 4 ; i ++)
    delete cards[i];
  delete cards;

  return 0;
}
