#include <iostream>
#include <string>
#include <fstream>

//int frac(int n);
using namespace std;

int main(int argc, const char *argv[])
{
  std::ifstream infile(argv[1]);
  int num;
  int k, c, s;

  infile >> num;
  for (int i = 0; i < num; i++){
    infile >> k >> c >> s;
    string str = "";
    for(int i = 1; i <= k; i++){
      if(i==1){
        str.append("1");
      }else{
        str.append(" " + to_string(i));
      }
    }
    cout << "Case #" + to_string(i + 1) + ": " + str << endl;
  }
  return 0;
}


