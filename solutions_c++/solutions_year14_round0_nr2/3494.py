#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char** argv){
  int T;
  double C, F, X;

  double r,tX,tC,tNextX;

  cin>>T;
  for(int i=0; i<T; i++){
    cin>>C>>F>>X;
  
    r=2.0;
    tC=0.0;
    do {
      tX=tC+X/r;
      tC+=C/r;
      r+=F;
      tNextX=tC+(X/r);
    } while(tNextX<tX);
       
    cout<<setprecision(10)<<"Case #"<<i+1<<": "<<tX<<"\n"; 
  }


  return 0;
}
