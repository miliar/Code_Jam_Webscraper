#include <fstream>
#include <cstdlib>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <vector>

void solve(std::ifstream& istr,std::ofstream& ostr,int Tcase);

int main(int argc,char *argv[]){
  if(argc < 2 || argc>2)
    return 1;
  std::ifstream istr(argv[1]);
  if(!istr){
    std::cerr << "cannot open specificed input file\n";
  }

  std::ofstream ostr("output.out");
  if(!ostr){
    std::cerr<"error openning output file\n";
    exit(1);
  }
  

  std::string cases;
  istr >> cases;
  int Tcases = atoi(cases.c_str());
  for(int i = 0;i<Tcases;i++){
    solve(istr,ostr,i+1);
  }
  
  return 0;
}


void solve(std::ifstream& istr,std::ofstream& ostr,int Tcase){
  std::string token;
  istr >> token;
  int max = atoi(token.c_str());
  std::vector<int> list;
  istr >> token;
  for(int i = 0;i<max+1;i++)
    list.push_back((int)token[i]-48);

  int ppl = list[0];
  int ans = 0;
  for(int i = 1;i<list.size();i++){
    if(list[i] != 0){//if there is someone at this shyness lvl
      if(ppl >= i) //is there enough ppl clapping to make S_i standup?
	ppl+= list[i];//if so add ppl at this lvl to ppl standing
      else{
	ans+= i - ppl;
	ppl+= ans + list[i];
      }
    }
  }
  //Case #1: 0

  ostr<<"Case #"<<Tcase<<": "<<ans<<"\n";  
}
  

