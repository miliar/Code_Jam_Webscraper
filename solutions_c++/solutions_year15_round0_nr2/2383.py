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
    int d,s,m,temp;
    int p[1000];
    for (int j=1; j<=t; j++){
          I >> d;
          m=0;
          for (int i=0; i<d; i++){
              I >> p[i];
              if (p[i]>m)
                 m=p[i];
          }
          s=m;
          for (int k=2; k<m; k++){
              temp=0;
              for (int i=0; i<d; i++)
                  temp+=((p[i]%k)?(p[i]/k+1):(p[i]/k))-1;
              s=min(s,temp+k);
          }
          O << "Case #" << j << ": " << s << "\n";                               
    }
    I.close();
    O.close();
    return 0;
}
