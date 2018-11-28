#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
  int testSample;
  int people;
  
  int sum;
  int needed;

  fstream fin;
  ofstream fout;
  fin.open("A.txt");

  if(!fin.good()){
    cout << "Error" << endl; 
    return 0;
  }

  fout.open("result.txt");

  fin >> testSample;
  cout << testSample;

  for (int i = 0; i < testSample; i++){
    
    string list;
    sum = 0;
    needed = 0;
    
    fin >> people;
    
    fin >> list;

    sum += (list[0] - '0');
    for (int j = 1; j <= people; j++){
      if (sum < j){
        needed += (j - sum);
        sum = j;
      }
      sum += (list[j] - '0');
    }

    fout << "Case #" << i+1 << ": " << needed << endl;

  }

  fin.close();
  fout.close();
  return 0;
}