#include <iostream> 
#include <fstream>
#include <string> 
#include <stdlib.h> 
#include <cstring>
using namespace std;

int main (int argc, char** args) { 
  ifstream in;
  in.open(args[1]);
  if (!in) { 
   cerr << "Can't open filebase.in" << endl; exit(2); 
  } 
  // read all input from in, write to cout 
  // in >> ... 
  // cout << ...
  ofstream out("output");
  int num;
  in >> num;
  for (long i = 0; i < num; i++) {
    out << "Case #" << i + 1 << ": ";
    char pancake[101];
    in >> pancake;
    int ptr = strlen(pancake) - 1;
    int count = 0;
    bool flag = true;
    while (ptr >= 0) {
        char verify = '+';
        if (!flag) {
            verify = '-';
        } 
        if (pancake[ptr] != verify) {
            count ++;
            flag = !flag;
        }
        ptr --;
    }

    out << count << endl;

    cout << "Finished " << i + 1 << " out of " << num << endl;
    
  }
  out.close();
  return 0; 
} 