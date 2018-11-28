#include <algorithm>
#include <iostream>
#include <cassert>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;
ifstream in("A-small.in");
ofstream out("out.out");
int caso,ncasi;
int main()
{
  in>>ncasi;
  for (caso=1;caso<=ncasi;caso++){
    int r,c,w,tot;
    in>>r>>c>>w;
    int cRiga=c/w;//i colpi che devo fare per forza in ogni riga
    tot=r*cRiga;
    if (c%w==0) tot+=w-1;//i colpi per affondare la nave
    else tot+=w;
    cout<<"Case #"<<caso<<": "<<tot<<endl;
    out<<"Case #"<<caso<<": "<<tot<<endl;
  }
}
