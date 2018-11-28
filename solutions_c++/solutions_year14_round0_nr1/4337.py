/****************************************************************
 * Magician
 * Author: Marcus Zeagler
 * Date last modified: 11 April 2014
 *
 * This program analysis a magic trick, where the same card is choosen
 * out of two seperated 4x4 grid of cards. And the magician guesses
 * the card choosen.
 *
 * Input: line 1 is number of tests,
 *        the rest of the input will be in groups of 10
 *        1. the first of these is the row from which a card is choosen
 *        2. the next 4 are the rows of cards
 *        the last 5 are the follow the format of 1 and 2
 *
 *        the program will expect the same number of groups as there are
 *        tests as determined by the first input number.
 *
 *
 * Output: the card choosen or an error in the trick
**/
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

///////////////////////////////////////////////////////////
// Read the input file, parsing it into a string vector
//
// input: the file name as string
// output: the vector containing input
///////////////////////////////////////////////////////////
vector<string> read_file(string file_name) {
  //Declare variables
  vector<string> in_file;
  string line;

  //open the file for reading
  ifstream the_file(file_name.c_str());
  if (the_file.is_open()) {
    //file is valid
    while (getline(the_file, line)) {
      in_file.push_back(line); //build the vector
    }
    the_file.close();
  } else {
    //file is invalid
    in_file.push_back("File could not be opened");
  }
  
  return in_file;
}

///////////////////////////////////////////////////////////
// Save the output 
//
// input: the vector containing output, the file name as string
// output: n/a
///////////////////////////////////////////////////////////
void write_file(vector<string> out_file, string file_name) {
  //open the file for writing
  ofstream the_file(file_name.c_str());
  if (the_file.is_open()) {
    for (int i = 0; i < out_file.size(); i++) {
      //loop through the vector
      //save to the file
      the_file << out_file[i];
    }
    the_file.close();
  }
}

int main(int argc, char *argv[]) {
  // I/O variables
  string inFileName;       //hold name of input file
  vector<string> in_file;  //hold input data
  vector<string> out_file; //hold output data

  cout << "Enter the input file: " << endl;
  cin >> inFileName;
  in_file = read_file(inFileName);
  
  //exit if file not found
  if (in_file[0] == "File could not be opened") {
    cout << "Input file could not be opened" << endl;
    return 0;
  }

  //
  //variables
  //
  int cases;      //number of cases
  int index = 0;  //for help parsing the file
  int i, j, k, l; //for iterators
  int an_answer;  //hold one answer
  int similar_card; //answer to the problem

  string output;        //hold the output
  string out_text;      //hold output text(Bad magician)
  string cards_in_row;  //hold a unseparated row of cards
  
  vector<int> the_answers;      //hold both answers in a case
  vector<int> a_row;            //hold one sepatrated row
  vector< vector<int> > a_grid; //hold one grid of row
  vector< vector< vector<int> > > the_grids; //hold both grids
  
  vector<int> temp_row_1; //will hold answer_1 row
  vector<int> temp_row_2; //will hold answer_2 row

  //
  //Work the data
  //
  //
  //extract number of cases in the file
  istringstream (in_file[index++]) >> cases;

  for (i = 1; i <= cases; i++) {

    //'reinitilize' variable
    a_row.clear();
    a_grid.clear();
    the_grids.clear();
    the_answers.clear();
    similar_card = 0;

    //get the answers and grids
    for (j = 0; j < 2; j++) {
      istringstream (in_file[index++]) >> an_answer;
      the_answers.push_back(an_answer);
      
      for (k = 0; k < 4; k++) {
          //get a row of cards
          cards_in_row = in_file[index++];
          istringstream iss(cards_in_row);

          //separate the cards
          while (iss >> l) {
            a_row.push_back(l);
            }
          
          //build a grid
          a_grid.push_back(a_row);
          a_row.clear();
      }

      the_grids.push_back(a_grid);
      a_grid.clear();
    }
	
    //analyse the grids
    temp_row_1 = the_grids[0][the_answers[0]-1]; 
    temp_row_2 = the_grids[1][the_answers[1]-1];

    //check each value in row_1 to row_2
    for (k = 0; k < 4; k++) {
      for (l = 0; l < 4; l++) {
        if (temp_row_1[k] == temp_row_2[l]) {
          if (similar_card == 0) {
            //if there is a match set similar_card to that card
            similar_card = temp_row_1[k]; 
          } else {
            //if similar card is already set, Bad Magician
            similar_card = -1;
          } //else no match, voulenteer cheated
        }
      }
    }

    //
    //output
    //
    ostringstream oss;
    oss << "Case #" << i << ": ";
    
    if (similar_card == -1) {
      oss << "Bad magician!\n";
    } else if (similar_card == 0){
      oss << "Volunteer cheated!\n";
    } else {
      oss << similar_card << "\n";
    }

    output = oss.str();
    out_file.push_back(output);
  }

  write_file(out_file, "data.out");
  return 0;
}