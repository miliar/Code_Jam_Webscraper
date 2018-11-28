#include <iostream>
#include <fstream>
#include <string>
#include <string.h>

using namespace std;

void read_input(void);
void process(void);
void write_output(void);

/* Global data */

ifstream ifile;
int num_cases;
string ostring = "";
//char filename[] = "A-small-attempt0.in";
char filename[] = "A-large.in";
//char filename[] = "test.in";

struct TestCaseType{
  int max_shy;
  string shy_str;
}test_case;

int needed = 0;

/* Functions */

// The data structure we read into may change
void read_test_case(void){
  ifile >> test_case.max_shy;
  ifile >> test_case.shy_str;
}

// Process the input
void process(void){
  int standing = 0;

  needed = 0;
  standing += test_case.shy_str[0] - (int)'0';
  for(int i=1; i<test_case.max_shy + 1; i++){
    if(standing < i){
      needed++;
      standing++;
    }
    standing += test_case.shy_str[i] - '0' ;
  }
}

// Builds the output string for the specified case
void case_output(int i){
  char case_str[100];

  snprintf(case_str, 100, "Case #%d: %d\n", i + 1, needed);
  ostring += string(case_str);
}

// Writes all the case results
void write_output(void){
  ofstream ofile;

  ofile.open("output.txt");
  ofile << ostring;
  ofile.close();
}

int main(int argc, char **argv){
  ifile.open(filename);
  ifile >> num_cases;
  for(int i=0; i<num_cases; i++){
    read_test_case();
    process();
    case_output(i);
  }
  ifile.close();
  write_output();
  return 0;
}
