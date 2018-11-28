#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <queue>

using namespace std;

int main()
{
    fstream I,O;
    I.open("in.txt");
    O.open("out.txt");
    int t;
    I >> t;
    int n,k,sum;
    string s;
    for (int j=1; j<=t; j++){
          I >> n >> s;
          k=0;
          sum=0;
          for (int i=0; i<n; i++){
              sum+=s[i]-'0';
              if (i+1>sum && s[i+1]){
                 k+=i+1-sum;
                 sum+=i+1-sum;
              } 
          }
          O << "Case #" << j << ": " << k << "\n";                               
    }
    I.close();
    O.close();
    return 0;
}
