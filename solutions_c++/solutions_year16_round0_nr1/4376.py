#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
  ifstream myInput;
  myInput.open("A-large.in");
  ofstream myOutput;
  myOutput.open("solution.out");

  int t;
  myInput >> t;
  for(int i = 0; i < t; i++)
  {
    bool array[10] = {0,0,0,0,0,0,0,0,0,0};
    string input;

    myInput >> input;
    if(input[0] == '0'){
      myOutput << "Case #" << i + 1 << ": INSOMNIA\n";
    }
    else{
      int orig = 0;
      for(int j = 0; j < input.length(); j++)
        orig = orig * 10 + (input[j] - 48);

      bool cont = 1;
      int count = 1;
      while(cont)
      {
        int add = 0;
        for(int k = input.length() - 1; k >= 0; k--)
        {
          int digit = (input[k] - 48);
          digit *= count;
          digit += add;
          if(digit > 9){
            add = digit / 10;
            digit -= (add * 10);
          }
          else{
            add = 0;
          }
          array[digit] = 1;
        }
        if(add)
          array[add] = 1;
        cont = 0;
        for(int l = 0; l < 10; l++)
        {
          if(array[l] == 0)
            cont = 1;
        }
        count++;
      }
      count--;
      myOutput << "Case #" << i + 1 << ": " << orig * count << endl;
    }
  }
}


/*int turns = 1;
bool cont = 1;
int leftover;

while(cont){
  int length = 1;
  while(input / length)
    length *= 10;
  length /= 10;
  for(int j = length; j > 0; j /= 10)
  {
    int used = input / j;
    array[]
  }
}*/
