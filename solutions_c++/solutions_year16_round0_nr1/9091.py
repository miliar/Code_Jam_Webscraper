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
char problem_name[] = "counting_sheep";
//char filename[] = "A-small-attempt0.in";
char filename[] = "A-large.in";
//char filename[] = "test.in";

struct TestCaseType{
  uint32_t N, last;
}test_case;

// index maps to digit. 1 for seen, 0 for unseen
uint8_t digits_seen[10];

/* Functions */

int all_seen(void){
  int all_seen = 1;
  for(int i=0; i<10; i++){
    all_seen *= digits_seen[i];
  }
}

void scan_digits(uint32_t num){
  uint32_t div = 1;
  uint32_t digit;
  if(num == 0){
    digits_seen[0] = 1;
  }
  else{
    while(div <= num){
      digit = (num / div) % 10;
      digits_seen[digit] = 1;
      div *= 10;
    }
  }
}

// The data structure we read into may change
void read_test_case(void){
  ifile >> test_case.N;
}

// Process the input
void process(void){
  uint32_t next_num, i;
  i = 0;
  while(next_num != 0){
    next_num = (i+1)*test_case.N;
    i++;

    // track digits present in next_num
    scan_digits(next_num);

    // if all 10 digits have been seen, end loop
    if(all_seen()){
      break;
    }
  }
  test_case.last = next_num;
}

// Builds the output string for the specified case
void case_output(int i){
  char case_str[100];

  if(test_case.last != 0){
    snprintf(case_str, 100, "Case #%d: %d\n", i + 1, 
             test_case.last);
  }
  else{
    snprintf(case_str, 100, "Case #%d: INSOMNIA\n", i + 1);
  }

  ostring += string(case_str);
}

void reset_state(void){
  for(int i=0; i<10; i++){
    digits_seen[i] = 0;
  }
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
