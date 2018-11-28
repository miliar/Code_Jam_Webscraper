#include<iostream>
#include <iomanip>
using namespace std;


double totalTime(double C,double F, double X, double rate, double time){
    double timeFinish = (X/rate) +time;
    double newRate = rate+F;
    double timeBuyFarm = (C/rate)+(X/newRate)+time;
   
    
    if(timeFinish <= timeBuyFarm)
      return timeFinish;
    else
      return totalTime(C,F,X,newRate,(C/rate)+time);
    
}

int main(){
    ios_base::sync_with_stdio(false);
    
    int t;
    cin >> t;
    
    for(int i=1;i<=t;i++){
      double C,F,X;
      cin >> C >> F >> X;
      cout << "Case #"<<i<<": ";
      
      cout << fixed << setprecision(7) << totalTime(C,F,X,2,0) << endl;
      
        
    }
}
