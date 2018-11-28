#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <algorithm>
#include <vector>
#include <cstring>
#include <stack>
#include <cctype>
#include <utility>
#include <map>
#include <string>
#include <climits>
#include <set>
#include <string>
#include <sstream>
#include <utility>
#include <ctime>
#include <iomanip>
using namespace std;
double c,f,x;
double timesum(int n){
  if((x/(2+(n*f)))<(c/(2+(n*f)))+(x/(2+((n+1)*f))))
    return (x/(2+(n*f)));
  else
    return ((c/(2+(n*f)))+timesum(n+1));
}

int main(){
  int t,n=1;
  cin>>t;
  while(t--){
    cin>>c>>f>>x;
    cout<<"Case #"<<n++<<": "<<fixed<<setprecision(7)<<timesum(0)<<endl;
  }
}
