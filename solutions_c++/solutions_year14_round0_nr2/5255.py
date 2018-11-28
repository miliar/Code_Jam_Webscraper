#include<iostream>
#include<iomanip>
using namespace std;

#define ld long double

int main (){
  int tes;
  cin>>tes;
  std::cout << std::setprecision(10) << std::fixed;
  for (int it = 1;it<=tes;++it){
    ld c, f, x, r(2), t(0);
    cin>>c>>f>>x;

    while (1){
      if ((x/r) < (c/r) + (x/(r+f))) break;
      else {t += (c/r);r+=f;}
    }
    t += x/r;

    cout<<"Case #"<<it<<": "<<t<<"\n";
  }
  return 0;
}
