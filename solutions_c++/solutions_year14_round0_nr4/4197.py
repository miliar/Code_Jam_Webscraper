/****************************************************************
 * Deceitful War
 * Author: Marcus Zeagler
 * Date last modified: 12 April 2014
 *
**/
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
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

  cout << "Enter the input file name: " << endl;
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

  int number_of_blocks;      //number of blocks each has
  double one_block;
  
  double temp_block_1;
  double temp_block_2;
  
  vector<double> naomi_blocks;  //hold naomi's blocks
  vector<double> ken_blocks;    //hold ken's blocks

  int decietful_score;
  int optimum_score;

  string input_line;    //hold one unparsed input line
  string output;        //hold one output line
  ostringstream oss;    //output stream

  //
  //Work the data
  //
  //
  //extract number of cases in the file
  istringstream (in_file[index++]) >> cases;

  for (int i = 1; i <= cases; i++) {
    //'reinitilize' variable
    temp_block_1 = 0;
    temp_block_1 = 0;
    number_of_blocks = 0;
    decietful_score = 0;
    optimum_score = 0;
    naomi_blocks.clear();
    ken_blocks.clear();
    oss.str("");
    oss << "Case #" << i << ": ";

    //get block data
    input_line = in_file[index++];
    istringstream iss(input_line);
    
    iss >> number_of_blocks;
    double l;
      
    input_line = in_file[index++];
    istringstream jss(input_line);
    
    //parse naomi's blocks
    for (int j = 0; j < number_of_blocks; j++) {
      jss >> l;
      naomi_blocks.push_back(l);
    }
    
    input_line = in_file[index++];
    istringstream kss(input_line);
    
    //parse ken's blocks
    for (int j = 0; j < number_of_blocks; j++) {
      kss >> l;
      ken_blocks.push_back(l);
    }
    
    sort(naomi_blocks.begin(), naomi_blocks.end());
    sort(ken_blocks.begin(), ken_blocks.end());

    //
    //decietful strategy
    //make ken play high blocks
    //
    //play lowest say it is higher
    //but less than ken's highest block
    //
    //
      decietful_score = naomi_blocks.size();
      vector<double> naomi = naomi_blocks;
      vector<double> ken = ken_blocks;
        
      for (int k = 0; k < number_of_blocks; k++) {
        for (int j = 0; j < naomi.size(); j++) {
          if (ken[j] > naomi[j]) {
            naomi.erase(naomi.begin()); 
            ken.erase(ken.end()-1);
 
            decietful_score--;
            break;
          }
        }
      }

    //
    //optimum strategy
    //naomi play lowest
    //ken play lowest that is > naomi's
    //if no block is higher, naomi gets a point
    //

    for (int k = 0; k < number_of_blocks; k++) {
      temp_block_1 = 0;
      temp_block_2 = 0;
      
      for (int j = 0; j < ken_blocks.size(); j++) {
        if (ken_blocks[j] > naomi_blocks[temp_block_1]) {
          temp_block_2 = j;
          break;
        }
      }

      if (naomi_blocks[temp_block_1] > ken_blocks[temp_block_2]) {
        optimum_score++;
      }
      
      naomi_blocks.erase(naomi_blocks.begin()); 
      ken_blocks.erase(ken_blocks.begin()+temp_block_2);
    }
    //
    //output
    //
    oss << decietful_score << " " << optimum_score << "\n";
    output = oss.str();
    out_file.push_back(output);
  }

  write_file(out_file, "data.out");
  return 0;
}