#include <iostream>
#include <cstdio>

using namespace std;

int main(){
  int n;
  cin >>n;
  for (int i=0; i<n; i++){
    double c,f,x,vystup=0,cps=2.0,cps2=2;
    cin >> c >> f >> x;
    vystup=c/cps;
    while (x/(cps+f)<(x-c)/cps){
      cps+=f;
      vystup+=c/cps;
      //cout <<"cps "<<cps<<endl;
      //cout <<"vystup "<<vystup<<endl; 
    }
    vystup+=(x-c)/cps;
    printf("Case #%d: %lf\n",i+1,vystup);
  }
    
}