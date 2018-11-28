#include <iostream>
#include <fstream>
using namespace std;

int ovation(int smax, int* n){
  int i, add, cpt = 0, res = 0;
  for(i=0; i <= smax; i++){
    cpt += n[i];
    
    if(!(cpt > i)){
      add = i + 1 - cpt; 
      res += add;
      cpt += add;
    }
  }

  return res;
}

int main(int argc, char** argv){
  int i,j,it,smax;
  char a;
  string line, word;
  int n[1001];

  if(argc != 2){
    cout << "task01 <input_file>" << endl;
    return 1;
  }

  ifstream file(argv[1]);

  if(!file){
    cout << "error: can't open the file." << endl;
    return 1;
  }
  
  
  file >> it;
  for(i = 0; i < it; i++){
    file >> smax;
    file.ignore();
    for(j = 0; j <= smax; j++){
      file.get(a);
      n[j] = a - '0';
    }
    cout << "Case #" << i+1 << ": " << ovation(smax, n) << endl; 
  }

  file.close();
  return 0;
}
