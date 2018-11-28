#include <iostream>
using namespace::std;

void print_output(int T, string output) {
	 	cout << "Case #" << T << ": " << output << endl;
}

void the_last_word(int T) {
  string input = "";
  string output = "";

  int length;

  getline(cin, input);
  length = input.length();

  for (int i=0; i<length; i++) {
    if(input[i] < output[0])
      output = output + input[i];
    else
      output = input[i] + output;
  }
  print_output(T, output);
}

int main(void) {
  string input = "";
  int T = 0;

  getline(cin, input);
  T = stoi(input);

  for(int t=0; t<T; t++) {
		the_last_word(t+1);
	}

  return 0;
}
