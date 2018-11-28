#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
ifstream in("A-small.in");
ofstream out("out.out");

int main()
{
  int n,nt,t,tmp;
  vector<int> alfabeto;
  vector<int> ripetizioni;
  in>>t;
  string s;
  for (int i=0;i<30;i++) alfabeto.push_back(0);
  for (int i=0;i<10;i++) ripetizioni.push_back(0);
  for (int nt=1;nt<=t;nt++){
    out<<"Case #"<<nt<<": ";
    for (int i=0;i<30;i++) alfabeto[i]=0;
    for (int i=0;i<10;i++) ripetizioni[i]=0;
    in>>s;
    for (int i=0;i<s.length();i++) alfabeto[s.at(i)-'A']++;
    ripetizioni.at(0)=alfabeto.at('Z'-'A');
    ripetizioni.at(2)=alfabeto.at('W'-'A');
    ripetizioni.at(6)=alfabeto.at('X'-'A');
    ripetizioni.at(7)=alfabeto.at('S'-'A')-ripetizioni.at(6);
    ripetizioni.at(5)=alfabeto.at('V'-'A')-ripetizioni.at(7);
    ripetizioni.at(4)=alfabeto.at('F'-'A')-ripetizioni.at(5);
    ripetizioni.at(3)=alfabeto.at('R'-'A')-ripetizioni.at(4)-ripetizioni.at(0);
    ripetizioni.at(8)=alfabeto.at('H'-'A')-ripetizioni.at(3);
    ripetizioni.at(9)=alfabeto.at('I'-'A')-ripetizioni.at(5)-ripetizioni.at(6)-ripetizioni.at(8);
    ripetizioni.at(1)=alfabeto.at('O'-'A')-ripetizioni.at(0)-ripetizioni.at(2)-ripetizioni.at(4);
    string ris;
    for (int i=0;i<10;i++){
      for (int j=0;j<ripetizioni.at(i);j++){
        ris.push_back(i+'0');
      }
      //cout<<ripetizioni.at(i);
    }
    out<<ris<<endl;
    //cout<<endl<<ris<<endl;
  }
  return 0;
}
