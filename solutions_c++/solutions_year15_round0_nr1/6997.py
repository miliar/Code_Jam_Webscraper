#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

int main() {
  ifstream infile;
  ofstream outfile;
  infile.open("quals_p1_large.txt");
  if(infile.fail()) {
    cout << "Didn't work" << endl;
  } else {
    cout << "Opened" << endl;
  }

  outfile.open("quals_p1_large_out.txt");
  if(outfile.fail()) {
    cout << "Didn't work" << endl;
  } else {
    cout << "Opened" << endl;
  }


  int num_tests, s_max, val, num_friends, current_count;

  infile >> num_tests;
  string shy_str, shy_sub_str;

  for(int i = 0; i < num_tests; i++) {
    infile >> s_max;
    infile >> shy_str;
    
    current_count = num_friends = 0;

    for(int j = 0; j < shy_str.length(); j++) {
      shy_sub_str = shy_str.substr(j,1);
      val = atoi(shy_sub_str.c_str());
      if(current_count >= j){
	current_count += val;
      } else{
	num_friends += (j - current_count);
	current_count += (val + (j - current_count));
      }
    }
    
    outfile << "Case #" << i + 1 << ": " << num_friends << endl;
  }

  return 0;
}