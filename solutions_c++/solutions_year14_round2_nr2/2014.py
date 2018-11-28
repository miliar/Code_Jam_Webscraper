#include <iostream>
#include <cmath>
#include <map>
#include <utility>
#include <iomanip>
#include <vector>
#include <string>
using namespace std;

long int cal(long a, long b, long k){
  long i,j,o,num;
  num = 0;
  for (i=0; i<a; i++){
    for (j=0; j<b; j++){
      if ((i&j)>=0 && (i&j)<k) num++;
    }
  }
  return num;
}

int main(){
  int ti,i,j,m;
  long int n,a,b,k;
  vector<string> v;
  string s;
  cin>>ti;
  for (i=1; i<=ti; i++){
    if (i>1) cout << endl;
    cout << "Case #" << i << ": ";
    cin>>a>>b>>k;
    n = cal(a,b,k);
    cout << n;
  }
  return 0;
}

