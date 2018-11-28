#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
using namespace std;

class StackOfPancakes {
private:
  int flips;
  vector<bool> flapjacks;
public:
  void setValues(string s){
    flips = 0;
    flapjacks.resize(s.length());
    for (int i = 0; i < s.length(); i++){
      if (s[i] == '+'){
        flapjacks[i] = true;
      }else{
        flapjacks[i] = false;
      }
    }
  }

  void flip(int pancake){
    flips += 1;
    for (int i = 0; i < pancake + 1; i++){
      flapjacks[i] = !flapjacks[i];

    }
  }

  int determineFlip(){
    for (int i = 0; i < flapjacks.size() - 1; i++){
      if (flapjacks[i] != flapjacks[i + 1]){
         return i;
       }
    }
    return -1;

   }
   int findFlipCount(){
     int cake;
     for (int j = 0; j < flapjacks.size(); j++){
       cake = determineFlip();
       if (cake == -1){
         if (flapjacks[0] == true){
           return flips;
         }else {return flips + 1;}
       }else{
         flip(cake);
       }
     }
     return flips;
   }
};

int main(){
  ofstream outputStream  ("CodeJam2Output.txt");
  ifstream inputStream  ("B-large.in");
  int cases;
  string pancakeStack;
  inputStream >> cases;
  for (int k = 1; k < cases + 1; k++){
    StackOfPancakes cakes;
    inputStream >> pancakeStack;
    cakes.setValues(pancakeStack);
    outputStream << "Case #" << k << ": " << cakes.findFlipCount() << endl;
  }
  outputStream.close();
  inputStream.close();
}
