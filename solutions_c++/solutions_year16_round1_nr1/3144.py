#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main() 
{
  int numInps = 0, i=0, j=0, numflips=0;
  string inp;
  //int in

  cin>>numInps;

  for (i=0; i < numInps; ++i) {
    cin>>inp;
    //cin>>in;
    string out = "";
    string null = "\0";

    for (int j = 0; j < inp.size(); ++j) {
      if (out.size() == 0) {
        out.insert(out.begin(),inp[j]);
        out += null; 
      }
      else {
        if (inp[j] >= out[0]) {
          out.insert(out.begin(), inp[j]);
          out += null; 
        }
        else {
          out = out+inp[j];
          out += null; 
        }
      }

    }

    cout<<"Case #"<<i+1<<": "<< out<<endl;
  }
  return 0;
}
