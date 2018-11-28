#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
ifstream in("D-small.in");
ofstream out("out.out");
int main()
{
  int t,nT,k,c,s;
  in>>nT;
  nT++;
  for (t=1;t<nT;t++){
    out<<"Case #"<<t<<":";
    in>>k>>c>>s;
    for (int i=1;i<=k;i++)
      out<<" "<<i;
    out<<endl;
  }
  return 0;
}
