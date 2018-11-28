  //TODO
  //open output
  //close output

  #include <stdlib.h>
  #include <stdio.h>

  #include <iostream>
  #include <vector>
  #include <algorithm>
  #include <fstream>
  #include <string>
  #include <sstream>
  #include <unordered_set>
  #include <stdlib.h>

  using namespace std;
  
  void addDigits(int N, unordered_set<int> &digits) {          
    if (N == 0) {
      digits.insert(N);
      return;
    }
    while (N != 0) {
      digits.insert(abs(N % 10));
      N = N / 10;
    }
  }
  
  int lastNumber(int N) {
	if (N == 0) {
	  return 0;
	}
	unordered_set<int> digits;
	int last = N;
	addDigits(last, digits);
	while (digits.size() < 10) {	
	  last = last + N;
	  addDigits(last, digits);
	}
	return last;
  }


  int main() {
	  ifstream input("in.txt");
	  FILE *out;
	  out = fopen("out.txt", "w");
	  string s;
	  getline(input, s);	  
	  size_t sz;
	  int T = stoi(s, &sz);
	  for (int i = 1; i <= T; ++i) {
		  // Input case
		  getline(input, s);
		  istringstream ss(s);
		  int N;
		  ss >> N;		  		  
		  int result = lastNumber(N);
		  if (result != 0) {
		    fprintf(out, "Case #%d: %d\n", i, result);
		  } else {
		    fprintf(out, "Case #%d: %s\n", i, "INSOMNIA");
		  }
	  }
	  input.close();
	  fclose(out);
	  return 0;
  }


