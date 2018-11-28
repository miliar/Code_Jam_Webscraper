#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <map>
#include <fstream>
#include <unordered_map>
#include <cstring>

using namespace std;

main (int argc, char const *argv[])
{

  ifstream fin;
  fin.open("B-large.in", ios_base::in);
  
  FILE *fout = fopen("gimmesomeoutput.out", "w");
  
  int t, T;
  fin>>T;
  
  for(t=0;t<T;t++){
  
    double C, F, X;
    fin>>C>>F>>X;
    
    double rithmos = 2;
    double total = 0;
    
    while((((total + X/rithmos)-(total + C/rithmos + X/(rithmos+F)))) > 0.000000001){
    
      total = total + C/rithmos;
      rithmos = rithmos + F;
    
    }
    
    total += X/(rithmos);
    
    fprintf(fout, "Case #%d: %.7f\n",t+1, total);
    
  }
  
  fin.close();
     
  fclose(fout);

  return 0;
}