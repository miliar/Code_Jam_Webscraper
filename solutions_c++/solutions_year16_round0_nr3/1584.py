#include <iostream>
#include <fstream>
#include <exception>
#include <stdexcept> 
#include <string>
#include <sstream> 

using namespace std;
using ccharp=const char *;
using charp=char *;

using xuint=unsigned __int64;  
using xint=_int64;            
using uint=unsigned int;

using byte=unsigned char *;


string file_path(ccharp path_in, ccharp name_in) {
  string to;
  to=path_in;
  to+=name_in;
  return to;
}


class mifstream : public std::ifstream {
public:
  mifstream(ccharp path_in, ccharp name_in) {
    string pathname=file_path(path_in, name_in);
    open(pathname);
    if (!is_open()) {
      ostringstream err;
      err<<"can not open infile="<<pathname;
      throw err.str();
    }
  }
  ~mifstream() {
    close();
  }
};

class mofstream : public std::ofstream {
public:
  mofstream(ccharp path_in, ccharp name_in) {
    string pathname=file_path(path_in, name_in);
    open(pathname);
    if (!is_open()) {
      ostringstream err;
      err<<"can not open outfile="<<pathname;
      throw err.str();
    }
  }
  ~mofstream() {
    close();
  }
};


int my_main(int ac, char *av[]);

int main(int ac, char *av[]) {
  int result=0;
  try {
    result=my_main(ac, av);
  }
  catch (const exception &e) {
    cout<<"exception="<<e.what()<<endl;
  }
  catch (ccharp s) {
    cout<<"exception="<<s<<endl;
  }
  catch (string s) {
    cout<<"exception="<<s<<endl;
  }
  catch (...) {
    cout<<"some exception"<<endl;
  }
  return 0;
}
