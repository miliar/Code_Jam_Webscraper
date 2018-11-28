#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{

  fstream fin;
  ofstream fout;

  fin.open("A.txt");
  if (!fin.good()){
    cout << "Error" << endl;
    return 0;
  }
  fout.open("result.txt");

  
  int testCases;
  int x, r, c, flag;

  fin >> testCases;

  for (int i = 0; i < testCases; i++){
    fin >> x >> r >> c;

    fout << "Case #" << i + 1 << ": ";
    if (x>=7 || (r*c) % x != 0){
      fout << "RICHARD" << endl;
      continue;
    }

    flag = 0;
    for (int j = 1; j < x; j++){
      if (x > 3 && j>1) flag = 1; 
      if (!(c >= j + flag && r >= x - j + 1 + flag)){
        if (!(r >= j + flag && c >= x - j + 1 + flag)){
          flag = 2;
//          cout << i << "th " << j << "," << x - j + 1 << endl;
          break;
        }
      }
    }
    
    if (flag == 2)
      fout << "RICHARD" << endl;
    else
      fout << "GABRIEL" << endl;

  }

  fin.close();
  fout.close();
  return 0;
}