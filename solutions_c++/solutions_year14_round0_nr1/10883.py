// Four rows of cards. 
// Two questions - Which row is the card in the first time 
// Which row is the card in the second time. 
#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <vector> 
#include <algorithm>

using namespace std;

int StringToNumber(string str) {
  istringstream ss(str);
  int Result;
  ss >> Result;
  return Result; 
}

vector<int> extract_ints(std::string str)
{
  vector<int> ret;
  string temp = "";  
  for(int i = 0; i < str.size() ; i++) {
    if(isdigit(str[i])) {
      temp += str[i];
    } else if((temp.size() == 1) || (temp.size() == 2)) {
      int num = StringToNumber(temp); 
      temp = "";
      ret.push_back(num); 
    }
  }
  if((temp.size() == 1) || (temp.size() == 2)) {
    int num = StringToNumber(temp); 
    temp = "";
    ret.push_back(num);
  }
  return ret; 
}

void OutputResult(int num_test_cases, ifstream & the_file)
{
  int relevant_card_set_1[4];
  int relevant_card_set_2[4];
  for(int i = 0; i < num_test_cases; i++) {
    vector<int> temp;
    string nextline = "";

    ///////////////////////////////////
    // Parsing the file to get the numbers.. 
    for(int j = 0; j < 2; j++) {
      // The first line - the choice the customer chooses; 
      getline(the_file, nextline); 
      int choice = StringToNumber(nextline);
    
      // The second to fifth line - the arrangement of the cards 
      // on the table
      for(int l = 0; l < 4; l++) {
	getline(the_file, nextline); 
	// Temp will contain the 4 integers
	temp  = extract_ints(nextline);
	if(choice-1 == l) {
	  for (int k = 0; k < 4; k++) {
	    if(j == 0) {
	      relevant_card_set_1[k] = temp[k];	
	    } else {
	      relevant_card_set_2[k] = temp[k];	
	    }
	  }
	}
      }
    }
    //////////////////////////////////////
    // Now the task is to find the common elements 
    // in the 2 relevant card sets.
    vector<int> v(4);
    vector<int>::iterator it;
    sort(relevant_card_set_1, relevant_card_set_1+4);
    sort(relevant_card_set_2, relevant_card_set_2+4);
    it = set_intersection (relevant_card_set_1, 
			   relevant_card_set_1 + 4, 
			   relevant_card_set_2, 
			   relevant_card_set_2 + 4, 
			   v.begin());
    v.resize(it-v.begin());
    
    // Our output.. 
    cout << "Case #" << i+1 << ": "; 
    if (v.size() == 1) {
      cout << *(v.begin()) << endl; 
    } else if(v.size() == 0) {
      cout << "Volunteer cheated!" << endl; 
    } else {
      cout << "Bad magician!" << endl; 
    }
  }
}

int main ( int argc, char *argv[] ) {
if ( argc != 2 ) // argc should be 2 for correct execution
  // We print argv[0] assuming it is the program name
  cout<<"usage: "<< argv[0] <<" <filename>\n";
 else {
   // We assume argv[1] is a filename to open
   ifstream the_file ( argv[1] );
   // Always check to see if file opening succeeded
   if ( !the_file.is_open() )
     cout<<"Could not open file\n";
   else {
     char x;
     string num_test_cases_str; 
     getline(the_file, num_test_cases_str);
     int num_test_cases = StringToNumber(num_test_cases_str);
     int card_set[2][16];
     int choices[2][num_test_cases];
     OutputResult(num_test_cases, the_file);
   }
 }
}

//FindMissingNumber(1
// the_file.get ( x ) returns false if the end of the file
//  is reached or an error occurs
// while ( the_file.get ( x ) )
//     cout<< x;
// the_file is closed implicitly here
