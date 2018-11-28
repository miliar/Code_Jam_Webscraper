#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

bool sleep(bool k[]);

int main(){
  int count, sheep;
  ifstream fin("A-large.in");
  if(fin.fail())
    return -1;
  ofstream fout("test.out");
  fin >> count;
  for(int i = 1; i <= count; i++){
    fin >> sheep;
    fout << "Case #" << i << ": ";
    if(sheep == 0)
      fout << "INSOMNIA\n";
    else{
      int num = sheep;
      bool tru[9];
      for(int j = 0; j < 10; j++)
        tru[j] = false;
      for(int j = 1; !sleep(tru); num += sheep){
        int test = num;
        while(test != 0){
          tru[test%10] = true;
          test /= 10;
        }
      }
      fout << num - sheep << endl;
    } 
  }
}


bool sleep(bool k[]){
  for(int i = 0; i < 10; i++)
    if(k[i] != true)
      return false;
  return true;
}

