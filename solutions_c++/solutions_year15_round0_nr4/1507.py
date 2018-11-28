#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <queue>
#include <math.h>

using namespace std;

int main()
{
    fstream I,O;
    I.open("in.txt");
    O.open("out.txt");
    int t;
    I >> t;
    int x,r,c;
    for (int j=1; j<=t; j++){
          I >> x >> r >> c;
          O << "Case #" << j << ": ";    
          if ((r*c)%x || max(r,c)<x || min(r,c)<x-1){
             O << "RICHARD" << "\n"; 
             continue;
          }
          O << "GABRIEL" << "\n";                                    
    }
    I.close();
    O.close();
    return 0;
}
