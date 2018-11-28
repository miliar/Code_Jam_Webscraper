/****************************************************************
 * CookieClick
 * Author: Marcus Zeagler
 * Date last modified: 12 April 2014
 *
 * This program computes the minimum time it would take to
 * win a game of CookieClick, given the winning amounts,
 * cost of a cookie farm and cookie/second benefit of the farms.
 *
 * You begin gaining 2 cookies/second, with each farm you buy, you
 * will get an extra F cookies/second.
 *
 * Input: line 1 is number of tests,
 *        the lines that follow must be in the following format.
 *        farm_cost farm_cps winning_amount
 *
 *        the program will expect the same number of lines as there are
 *        tests as determined by the first input number.
 *
 *
 * Output: the time it will take in seconds
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

  double C;  //cost for cookie farm
  double F;  //additional cookies per second per farms
  double X;  //winning cookie amount

  double cookies_per_second;
  double time_to_farm;
  double time_to_win;
  double time_with_farm; // time to win if a farm is bought
  double elapsed_time;   // total time taken

  string input_line;    //hold one unparsed input line
  string output;        //hold one output line

  //
  //Work the data
  //
  //
  //extract number of cases in the file
  istringstream (in_file[index++]) >> cases;

  for (int i = 1; i <= cases; i++) {
    //'reinitilize' variable
    cookies_per_second = 2.0;
    time_to_farm = 0.0;
    time_to_win = 0.0;
    time_with_farm = 0.0;
    elapsed_time = 0.0;

    //get farm data
    input_line = in_file[index++];
    istringstream iss(input_line);

    iss >> C; //farm cost
    iss >> F; //+cookies per farm
    iss >> X; //winning amount

    time_to_farm = C / cookies_per_second;
    time_to_win = X / cookies_per_second;
    time_with_farm = X / (cookies_per_second + F) + time_to_farm;

    //if a farm decreases overall time
    while(time_with_farm < time_to_win) {
      elapsed_time += time_to_farm;
      cookies_per_second += F;
      
      time_to_farm = C / cookies_per_second;
      time_to_win = X / cookies_per_second;
      time_with_farm = X / (cookies_per_second + F) + time_to_farm;
    }

    elapsed_time += time_to_win;
    //
    //output
    //
    ostringstream oss;
    oss.precision(7);
    oss << "Case #" << i << ": " << fixed << elapsed_time << "\n";

    output = oss.str();
    out_file.push_back(output);
  }

  write_file(out_file, "data.out");
  return 0;
}