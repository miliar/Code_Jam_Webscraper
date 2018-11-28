#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

int main () {
  string line;
  int T,X,R,C;
  //ifstream myfile ("case.txt");
  ifstream myfile ("D-small-attempt1.in");
  std::ofstream out("out.txt");
  std::streambuf *coutbuf = std::cout.rdbuf();
  std::cout.rdbuf(out.rdbuf());
  int found= 0;
  if (myfile.is_open())
  {
    myfile >> T;
    for(int k=0;k<T;k++)
    {
	    myfile >> X;
            myfile >> R;
            myfile >> C;
            found= 0;
            //if (R*C % X != 0) found =1; 
            //if (R*C <= X) found =1; 
            //if ((X>R) && ( X>C)) found =1; 
            if(X==1) found =0;
            if(X==2) found =1;
            if((X==2) && (R*C % X == 0)) found =0;
            if(X==4) found =1;
            if((X==4) && (R*C == 16)) found =0;
            if((X==4) && (R*C == 12)) found =0;
            if(X==3) found =1;
            if((X==3) && (R*C == 6)) found =0;
            if((X==3) && (R*C == 9)) found =0;
            if((X==3) && (R*C == 12)) found =0;
            if(found ==0) cout << "Case #" << k+1 <<": " << "GABRIEL" << endl;
            else cout << "Case #" << k+1 <<": " << "RICHARD" << endl;
     }
     myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
