#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>     /* atoi */

using namespace std;

int casetable[10];

void initialize(){
  for (int i = 0; i < 10; i++) {
    casetable[i] = 0;
  }
}

void populate(long lm){
  string nm = to_string(lm);
  char a;
  for (int i=0; i<nm.length(); i++){
    a = nm.at(i);

    //cout << endl << atoi(&a) << endl;
    if (casetable[atoi(&a)] == 0){
       casetable[atoi(&a)] = 1;
     }
  }
}

int check(){
  for (int i = 0; i < 10; i++) {
    if (casetable[i] == 0){
      return 0;
    }
  }
  return 1;
}

// void printcasetable (){
//   for (int i = 0; i < 10; i++) {
//     cout << casetable[i];
//   }
// }

int main (int argc,char *argv[]){
  unsigned long number;
  unsigned long base_number;
  int pol;
  int flag =0;
  string line;
  ifstream myfile (argv[1]);

  if (myfile.is_open())
  {
    //std::string::size_type sz;   // alias of size_t

    // do stuff
    //delete [] cstr;
    getline (myfile,line);
    // char *cstr = new char[line.length() + 1];
    //strcpy(cstr, line.c_str());
    //myfile >> line;
    int cases = stoi(line);

    for (int i = 0; i < cases; i++) {
      getline (myfile,line);
      number = stol(line);
      base_number = number;
      initialize();
      pol = 1;
      while (check() == 0 ) {
        number = base_number * pol;

        populate(number);
        // cout<<endl;
        // printcasetable();
        pol++;
        if (number == base_number * pol ){
          cout<<"Case #" << i+1 <<": " << "INSOMNIA"<< endl;
          flag = 1;
          break;
        }
      }
      if (flag !=1){
        cout<<"Case #" << i+1 <<": " << number<< endl;
      } else {
        flag =0;
      }


      //std::cout << number << std::endl;
    }

    myfile.close();
  }
  else cout << "Unable to open file";

  return 0;
}
