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
	  for (int iter = 1; iter <= T; ++iter) {
		  // Input case
		  getline(input, s);
		  vector<char> pancakes;
		  pancakes.push_back(s[0]);
		  for (int i = 0; i < s.size(); ++i) {
		    if (s[i] != pancakes[pancakes.size()-1]) {		    
		      pancakes.push_back(s[i]);
		    }
		  }		  
		  int result;
		  if (pancakes[0] == '-') {		  
		    result = 1;
		  } else {		  
		    result = 0;
		  }
		  for (int i = 1; i < pancakes.size(); ++i) {		  
		    if (pancakes[i] == '-') {		    
		      result += 2;
		    }
		  }		  
		  fprintf(out, "Case #%d: %d\n", iter, result);		 
	  }
	  input.close();
	  fclose(out);
	  return 0;
  }


