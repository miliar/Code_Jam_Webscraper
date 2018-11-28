#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main() 
{
  int numInps = 0, i=0, j=0, numflips=0;
  string inp;
  char sym=' ';

  cin>>numInps;

  for (i=0; i < numInps; ++i) {
    cin>>inp;

    numflips = 0;
    if (strcmp(inp.c_str(), "+") == 0) {
      cout<<"Case #"<<i+1<<": 0"<<endl;
      continue;
    }

    if (strcmp(inp.c_str(), "-") == 0) {
      cout<<"Case #"<<i+1<<": 1"<<endl;
      continue;
    }

    sym = inp[0];
    for (j=1; j<inp.size(); ++j) {
       if (sym != inp[j]) {
         numflips++;
         sym = inp[j];
       }
    }
    if (sym == '-')
      numflips++;
    cout<<"Case #"<<i+1<<": "<<numflips<<endl;
  }
  return 0;
}
