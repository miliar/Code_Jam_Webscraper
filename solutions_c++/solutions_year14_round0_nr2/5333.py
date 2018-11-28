#include <iostream>
#include <iomanip>
using namespace std;

#define Rep(i,n) for(int i=0;i<(n);++i)

int main() {
  int ntest;
  cin >> ntest;
  Rep(t,ntest){
    double c, f, x;
    cin>>c>>f>>x;
    double cur_prod=2;
    double cur_time=0;
    double best=1e11;
    Rep(nf,1000000){
      best=min(best,x/cur_prod+cur_time);
      cur_time+=c/cur_prod;
      cur_prod+=f;
    }
    cout<<"Case #"<<t+1<<": "<<fixed<<setprecision(10)<<best<<endl;
  }
  return 0;
}
