#include "iostream"
#include <fstream>
using namespace std;
#define SIZE 4
int main(int argc, char const *argv[])
{
  ofstream myfile;
  myfile.open ("output.txt");
  int first[SIZE][SIZE], second[SIZE][SIZE];
  int cases, row;
  cin >> cases;
  for(int c=0; c<cases; ++c){
    int first_row, second_row;
    
    cin >> first_row;
    for(int i=0; i<SIZE; i++)
        for(int j=0; j<SIZE; j++)
          cin >> first[i][j];

    cin >> second_row;
    for(int i=0; i<SIZE; i++)
        for(int j=0; j<SIZE; j++)
          cin >> second[i][j];

    int found_number, correct=0;
    for(int i=0; i<SIZE; i++)
        for(int j=0; j<SIZE; j++){
          if (first[first_row-1][i]==second[second_row-1][j]){
            found_number = second[second_row-1][j];
            if(++correct > 1) break;
          }
        }
    if(correct == 1)
      myfile << "Case #" << c+1 << ": " << found_number << endl;
    else if(correct>1)
      myfile << "Case #" << c+1 << ": Bad magician!" << endl;
    else
      myfile << "Case #" << c+1 << ": Volunteer cheated!" << endl;
  }
  return 0;
}