#include <iostream>
#include <string>

using namespace std;

void pancakes(int ncase, string stack){
  int flips = 0;
  char previous = stack[0];
  //if(previous=='-')
    //++flips;
  for(int i=1;i<stack.length();++i){
    if(previous!=stack[i]){
      ++flips;
      previous = stack[i];
    }
  }
  if(previous=='-')
    ++flips;
  cout << "Case #" << ncase << ": " << flips << endl;
}

int main(){
  int ncases;
  cin >> ncases;
  for(int i=1;i<=ncases;++i){
    string stack;
    cin >> stack;
    pancakes(i, stack);
  }
  return 0;
}
