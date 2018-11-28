#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  ifstream myInput;
  myInput.open("D-small-attempt0.in");
  ofstream myOutput;
  myOutput.open("solution.out");

  int t;
  myInput >> t;

  for(int i = 0; i < t; i++){
    int k;
    int c;
    int s;
    myInput >> k >> c >> s;

    myOutput << "Case #" << i + 1 << ":";
    for(int j = 1; j <= s; j++)
      myOutput << " " << j;
    myOutput << endl;
  }
}
