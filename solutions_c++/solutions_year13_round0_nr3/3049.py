#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;
int num_array[100];

int main() {
  ifstream infile;
  ofstream outfile;
  infile.open("test.txt");
  if(infile.fail()) {
    cout << "Didn't work" << endl;
  } else {
    cout << "Opened" << endl;
  }
  
  outfile.open("Codejamtest.txt");
  if(outfile.fail()) {
    cout << "Didn't work" << endl;
  } else {
    cout << "Opened" << endl;
  }

  int num_tests, str_length, is_palindrome, count, num_a, num_b;
  int a, b, temp, iterator;

  infile >> num_tests;

  for(int z = 1; z <= num_tests; z++) {
    count = 0;
    infile >> a >> b;
    for(int i = a; i <= b; i++){
      is_palindrome = 1;
      temp = i;
      iterator = 0;
      while(temp != 0) {
	num_array[iterator] = temp % 10;
	temp /= 10;
	iterator++;
      }

      for(int k = 0; k < iterator; k++) {
	if(num_array[k] != num_array[iterator - k - 1]) {
	  is_palindrome = 0;
	}
      }

      int root = sqrt(i);

      temp = root;
      iterator = 0;
      while(temp != 0) {
	num_array[iterator] = temp % 10;
	temp /= 10;
	iterator++;
      }

      for(int k = 0; k < iterator; k++) {
	if(num_array[k] != num_array[iterator - k - 1]) {
	  is_palindrome = 0;
	}
      }
      

      if(is_palindrome == 1 && i == root * root) {
	cout << i << endl;
	count++;
      }
    }      
    outfile << "Case #" << z << ": " << count << endl;
  }
  return 1;
} 
