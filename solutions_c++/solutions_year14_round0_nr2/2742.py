#include<iostream>
#include<vector>
#include<cstdio>
#include<iomanip>

using namespace std;

int main(){
  int T;
  cin>>T;
  for(int case_count = 1;case_count <= T;case_count++){
    double C,F,X,rate = 2.0,time = 0.0, t1, t2, oldt2 = 999999999.0;
    scanf("%lf %lf %lf",&C,&F,&X);
    
    while (1){
      //      cout<<time+C/rate<< " " << time + X / rate<<endl;
      t1 = time + C / rate;
      t2 = time + X / rate;
      
      if (t2 > oldt2){
        time = oldt2;
        break;
      }
      oldt2 = t2;
      time += C / rate;
      rate += F;
    }
    cout<<"Case #"<<case_count<<": "<<std::fixed<<std::setprecision(7)<<time<<endl;
  }
  return 0;
}
