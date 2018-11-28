#include <algorithm>
#include <iostream>
#include <cassert>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;
ifstream in("C-small.in");
ofstream out("out.out");
int caso,ncasi;
int main()
{
  in>>ncasi;
  for (caso=1;caso<=ncasi;caso++){
    int d,c,v,nNuove=0,tmp;
    vector<int>val;
    vector<int>div;
    vector<bool>somme;
    in>>c>>d>>v;
    for (int i=0;i<d;i++){in>>tmp;div.push_back(tmp);somme.push_back(false);}
//    for (int i=0;i<d;i++){
//      for(int j=i+1;j<d;j++){
//        if (div.at(i)+div.at(j)>v)break;
//        for (int z1=1;z1<=c;z1++){
//          for (int z2=1;z2<=c;z2++) {val.push_back(div.at(i)*z1+div.at(j)*z2);}
//        }
//      }
//    }
    for (int i=0;i<div.size();i++)cout<<div.at(i)<<" ";
    cout<<endl;
    somme.at(somme.size()-1)=true;
    while (true){
      int tmp=0;
      for (int i=0;i<somme.size();i++){
        if (somme.at(i)) tmp+=div.at(i);
        if (tmp>v) break;
      }
      if (tmp<=v)val.push_back(tmp);
      //vado al successivo
      int con=1;
      while (con<=somme.size() && somme.at(somme.size()-con) ) {somme.at(somme.size()-con)=false; con++;}
      if (con>somme.size()) break;
      else somme.at(somme.size()-con)=true;
    }
    unique(val.begin(),val.end());
    sort(val.begin(),val.end());
    for (int i=0;i<val.size();i++)cout<<val.at(i)<<" ";
    cout<<endl;
    for(int i=1;i<=v;i++){
      if (!binary_search(val.begin(),val.end(),i)){
        val.push_back(i);
        for (int i=0;i<somme.size()-1;i++)somme.at(i)=false;
        somme.at(somme.size()-1)=true;
        while(true){
          int tmp=i;
          for (int i=0;i<somme.size();i++){
            if (somme.at(i)) tmp+=div.at(i);
            if (tmp>v) break;
          }
          if (tmp<=v)val.push_back(tmp);
          //vado al successivo
          int con=1;
          while (con<=somme.size() && somme.at(somme.size()-con) ) {somme.at(somme.size()-con)=false; con++;}
          if (con>somme.size()) break;
          else somme.at(somme.size()-con)=true;
        }
        div.push_back(i);
        somme.push_back(false);
        nNuove++;
  //      for(int j=i;j<=d;j++){
  //        for (int z1=1;z1<=c;z1++){
  //          for (int z2=1;z2<=c;z2++) val.push_back(i*z1+div.at(j)*z2);
  //        }
  //      }
        unique(val.begin(),val.end());
        sort(val.begin(),val.end());
      }
    }
    cout<<"Case #"<<caso<<": "<<nNuove<<endl;
    out<<"Case #"<<caso<<": "<<nNuove<<endl;
  }
}
