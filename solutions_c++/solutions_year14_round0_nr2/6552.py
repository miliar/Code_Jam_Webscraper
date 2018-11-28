#include<iostream>
#include<iomanip>

int main(){
  int n;
  std::cin >> n;
  std::cout << std::setprecision(10);
  for(int prob=1;prob<=n;prob++){
    double c,f,x;
    std::cin >> c >> f >> x;
    std::cout << "Case #" << prob << ": ";
    double t=0.000000001;
    double cps=2.0;
    while(1){
      double mt=x/cps;
      double bt=c/cps+x/(cps+f);
      if(mt<bt){
        std::cout << t+mt;
        break;
      }else{
        t+=c/cps;
        cps+=f;
      }
    }
    std::cout << std::endl;
  }
  return 0;
}