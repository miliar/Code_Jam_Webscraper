#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
using namespace std;
ifstream in("A-small.in");
ofstream out("out.out");
string word,inS;
int main()
{
  int t,nT,n;
  in>>nT;
  nT++;
  for (t=1;t<nT;t++){
    out<<"Case #"<<t<<": ";
    in>>inS;
    word.clear();
    word.push_back(inS.at(0));
    bool inizio;
    for (int i=1;i<inS.size();i++){
      for (int j=0;j<word.size();j++){
        if (word.at(j)<inS.at(i))
          {inizio=true; break;}
        else if (word.at(j)>inS.at(i))
          {inizio=false; break;}

      }
      if (inizio)
        word.insert(word.begin(),inS.at(i));
      else
        word.push_back(inS.at(i));
    }
    out<<word<<endl;
  }
  return 0;
}
