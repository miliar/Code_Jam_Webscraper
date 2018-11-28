#include <iostream>
#include <vector>
#include <algorithm>    // std::sort
#include <stdio.h>
using namespace std;

int main(){
  int T;
  cin>>T;
  for (int i=1;i<=T;i++){
    double c,f,x,ans;
    cin >>c>>f>>x;
    double s=2.0;
    double time=0.0;
    ans=x/s;
    while (true){
      time+=c/s;
      s+=f;
      double val=x/s+time;
      if ( val < ans) {ans=val;continue;}
      else break;
    }
    cout <<"Case #"<<i <<": ";
    printf ("%0.7f\n",ans);
   }
 return 0;
}
