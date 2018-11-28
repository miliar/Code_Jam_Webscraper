#include<iostream>
#include <string.h>

using namespace std;

int main()
{
  unsigned int numInps = 0, inVal = 0, val = 0, maxVal = 0, mul = 0;
  int i = 0, j = 0, digits = 0, digit = -1;
  int digarr[10] = {0,0,0,0,0,0,0,0,0,0}; 

  cin>>numInps;

  for (i=0; i<numInps; ++i) {
    memset(digarr, 0, 10*sizeof(int));
    mul = 0;
    digits = 0;
    cin>>inVal;
    if (!inVal) {
      cout<<"Case #"<<i+1<<":"<<" INSOMNIA"<<endl;
      continue;
    }
    do {
      ++mul;
      maxVal = inVal*mul;
      val = maxVal;
      while (val != 0) {
        
        digit = val%10;
        val = val/10;
        
        if ((digit !=-1) && (digarr[digit] == 0)) {
          digits++;
          digarr[digit] = 1;
        }
      }
    } while (digits < 10);

    cout<<"Case #"<<i+1<<": "<<maxVal<<endl;
  }
  return 0;
}
