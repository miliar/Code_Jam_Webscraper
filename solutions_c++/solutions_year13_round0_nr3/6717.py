#include <iostream>
#include <vector>
#include <string>

using namespace std;

int nextSq(int in)
{
  int out=1;
  while(out*out < in) out++;
  return out;
}

bool isPalin(int in)
{
  string test=to_string(in);
  for(int i=0;i<(test.size())/2;i++) {
    if(test[i]!=test[test.size()-1-i]) return false;
  }
  return true;
}

int main()
{
  int probsize;
  cin>>probsize;
  for(int idx=1; idx<=probsize; idx++) {
    int low, hi;
    cin>>low>>hi;
    int start=nextSq(low);
    int numfair=0;
    while(start*start<=hi) {
      if(isPalin(start*start) && isPalin(start)) {
	numfair++;
      }
      start++;
    }
    cout<<"Case #"<<idx<<": ";
    cout<<numfair<<endl;
  }
  
  return 0;
}
