#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;



int main(int argc, char* argv[]){

  ifstream in_str(argv[1]);

  if (!in_str.good()) {
    std::cerr << "Can't open " << argv[1] << " to read.\n";
    return 0;
  }

  ofstream out_str(argv[2]);

  if (!out_str.good()) {
    std::cerr << "Can't open " << argv[2] << " to write.\n";
    return 0;
  }

  int caseNum;
  in_str>>caseNum;
  int x, r, c;

  int caseCount = 1;
  while(in_str>>x>>r>>c){


    out_str<<"Case #"<<caseCount<<": ";
    caseCount++;

    int product = r*c;
    if(x == 1)
      out_str<<"GABRIEL"<<endl;

    else if(x == 2 && product%2 == 0)
      out_str<<"GABRIEL"<<endl;

    else if(r==1 && c==x) 
      out_str<<"RICHARD"<<endl;
    else if(r==x && c==1) 
      out_str<<"RICHARD"<<endl;

    else if(product%x == 0 ) {
      if((r>=c && c>= x)||(r>=c && x-c == 1))
        out_str<<"GABRIEL"<<endl;  
      else if((c>=r && r>= x)||(c>=r && x-r == 1))
        out_str<<"GABRIEL"<<endl; 
      else
        out_str<<"RICHARD"<<endl;
    }

    else
      out_str<<"RICHARD"<<endl;

  }



  return 0;
}