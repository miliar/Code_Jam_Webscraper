#include <cstdio>
#include <iostream>
#include <istream>
#include <ostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <iomanip>
#include <sstream>
#include <fstream>

using namespace std;

bool check(long num){
 long str = num;
 long r = 0;
 int digit = 0;
 while (num > 0)
 {
      digit = num % 10;
      r = r * 10 + digit;
      num = num / 10;
 }
 if (str == r) {
 return true;}
 else{
 return false;}
}

int main () {
  string line;
  long n;
  long a;
  long b;
  long count;
  long x = 0;
  ofstream outputFile;
  outputFile.open("outputC.txt");
  ifstream myfile;
  myfile.open("exampleC.txt");
  if (myfile.is_open())
  {
  myfile >> n;
    for (long i = 1; i <= n; i++){
        count = 0;
        myfile >> a;
        myfile >> b;
        if ((int)sqrt(a)*(int)sqrt(a) != a) 
        a = (int)sqrt(a)+1;
        else
        a = (int)sqrt(a);
        b = (int)sqrt(b);
    for (long j = a; j <= b; j++){
        if  (check(j)){
            if (check(j*j)){
            count++;
            }
            }
        }
        cout << count;
        outputFile << "Case #"<<i<<": "<<count<<endl;
     }
    myfile.close();
    outputFile.close();
  }

  else cout << "Unable to open file"; 
  system("pause");
  return 0;
}
