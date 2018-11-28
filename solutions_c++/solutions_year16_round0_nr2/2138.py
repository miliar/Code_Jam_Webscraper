#include <iostream>
using namespace std;

static int mycount(char *mystring) {
  int mylen = 0, numflip = 0, start = 0, found = 0;
  int i = 0;
  if (mystring == NULL)
	  return 0;
  mylen = strlen(mystring);
  
  if (mystring[0] == '-') {
	  numflip++;
	  start = 1;
  }

  for (i = 0; i < mylen; i++) {
	  if (start == 1 && (mystring[i] == '-')) {
        continue;
	  }

	  if (mystring[i] == '+') {
        start = 0;
		found = 1;
	  } else if (found == 1){
	     found = 0;
         numflip += 2;
	  }
  }
  return numflip;
}

int main() {
  int numflip = 0, i = 0;
  int num_test;
  char panstring[102];
  memset(panstring, '\0', 102);
  cin >> num_test;
  for (i = 0; i < num_test; i++) {
    cin >> panstring;
    numflip = mycount(panstring);
	cout <<"Case #"<<i+1<<": "<<numflip<<"\n";

  }
  return 0;
}