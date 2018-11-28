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
  int sMax;
  string theString;

  int caseCount = 1;
  while(in_str>>sMax>>theString){

    //cout<<sMax<<"   "<<theString<<endl;

    out_str<<"Case #"<<caseCount<<": ";
    caseCount++;

    /*
    stringstream ss;
    ss << sMax;
    string s = ss.str();
    */
    //string s = to_string(sMax);

    string s = theString;

    int pCount = 0;
    int pNeed = 0;
    for(int i = 0; i< s.size(); i++){

      if(pCount <= i && (int)s[i] - '0' != 0){
        pNeed += i - pCount;
        pCount = i;
      }

      pCount += (int)s[i] - '0';
      //cout<<pCount<<" "<<pNeed<<" "<<(int)s[i] - '0'<<" "<<s[i]<<endl;

    }
    out_str<<pNeed<<endl;




  }



  return 0;
}