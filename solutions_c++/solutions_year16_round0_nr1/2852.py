#include <iostream> 
#include <fstream>
#include <string> 
#include <stdlib.h> 
using namespace std;

// data typically longo global variables here
bool check(long a[]) {
    for (long i = 0; i < 10; i++) {
        if (a[i] == 0) {
            return false;
        }
    }
    return true;
}

void setUp(long* arr, long sheep) {
    while (sheep != 0) {
        int m = sheep % 10;
        arr[m] ++;
        sheep = sheep / 10;
    }
}

int main (int argc, char** args) { 
  ifstream in;
  in.open(args[1]);
  if (!in) { 
   cerr << "Can't open filebase.in" << endl; exit(2); 
  } 
  // read all input from in, write to cout 
  // in >> ... 
  // cout << ...
  ofstream out("output.ini");
  long num;
  in >> num;
  for (long i = 0; i < num; i++) {
    out << "Case #" << i + 1 << ": ";
    long sheep;
    in >> sheep;
    long remember[10] = {};
    long count = 0;
    long ori = sheep;
    if (sheep == 0) {
        out << "INSOMNIA" << endl;
        continue;
    } else {
        while (!check(remember)) {
            setUp(remember, sheep);
            count ++;
            sheep += ori;
        }
        out << count * ori << endl;
        cout << "Finished " << i + 1 << " out of " << num << endl;
    }
  }
  out.close();
  return 0; 
} 