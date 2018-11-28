#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>     /* atoi */

using namespace std;

char stack[100];
int stack_size;
int steps;

void printstack (){
  for (int i = 0; i <stack_size; i++) {
    cout << stack[i];
  }
  cout <<endl;
}

void myReverse(int bot){
  steps++;
  int tmpBot = bot;
  char swapVal;
  string lola;

  for (int i = 0; i <= bot/2; i++) {
    swapVal = stack[tmpBot];
    if (stack[i]=='-'){
      stack[tmpBot]='+';
    }
    else {
      stack[tmpBot]='-';
    }

    if (swapVal=='-'){
      stack[i]='+';
    }
    else {
      stack[i]='-';
    }
    tmpBot--;
  }
  //cin >> lola;

  //cout << "bottom : "<< bot<<endl;
  //printstack();
}

int main (int argc,char *argv[]){
  string line;
  ifstream myfile (argv[1]);
  int bottom, top;

  if (myfile.is_open())
  {
    getline (myfile,line);
    int cases = stoi(line);

    for (int i = 0; i < cases; i++) {
      steps=0;
      getline (myfile,line);
      stack_size = line.length();
      bottom = stack_size-1;
      for (int i = 0; i <stack_size; i++) {
        stack[i]= line.at(i);
      }
      // cout<<"====================================================================================="<<endl;
      //   printstack();

      while (bottom!=-1){
        if (stack[bottom]=='+'){
          bottom--;
          continue;
        }
        else {
          if (stack[0] == '-'){
            myReverse(bottom);
          } else {
            for (int j = 0; j <= bottom; j++) {
              if (stack[j]=='+') {
                continue;
              } else {
                myReverse(j-1);
                break;
              }
            }
          }
        }
      }


      cout<<"Case #" << i+1 <<": " << steps << endl;

    }

  }

  myfile.close();

}
