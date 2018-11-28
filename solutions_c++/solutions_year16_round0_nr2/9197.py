#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <stdint.h>

using namespace std;

void read_input(void);
void process(void);
void write_output(void);

/* Global data */

ifstream ifile;
int num_cases;
string ostring = "";
char problem_name[] = "revenge_pancakes";
//char filename[] = "B-small-attempt0.in";
char filename[] = "B-large.in";
//char filename[] = "test.in";

struct TestCaseType{
  uint8_t cakes[100];
  int length;
  uint32_t flips;
}tc;

/* Functions */

// The data structure we read into may change
void read_test_case(void){
  string s;
  ifile >> s;
  tc.length = s.length();
  for(int i=0; i<tc.length; i++){
    if(s[i] == '+'){
      tc.cakes[i] = 1;
    }
    else{
      tc.cakes[i] = 0;
    }
  }
}

void flip(int index){
  for(int i=0; i<=index; i++){
    tc.cakes[i] ^= 1;
  }
  tc.flips++;
}

// Process the input
void process(void){
  // find the first cake from the bottom that isn't happy up (1)
  for(int i=tc.length-1; i>=0; i--){
    if(tc.cakes[i] != 1){
      // flip all cakes from that position up
      flip(i);
    }
  }
}

// Builds the output string for the specified case
void case_output(int i){
  char case_str[100];

  snprintf(case_str, 100, "Case #%d: %u\n", i + 1, 
           tc.flips);

  ostring += string(case_str);
}

void reset_state(void){
  memset(&tc, 0, sizeof(tc));
}

// Writes all the case results
void write_output(void){
  ofstream ofile;
  char ofilename[100];

  snprintf(ofilename, 100, "output--%s--%s.txt", problem_name, strtok(filename, "."));
  ofile.open(ofilename);
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
    reset_state();
  }
  ifile.close();
  write_output();
  return 0;
}
