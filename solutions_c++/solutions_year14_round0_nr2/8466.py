#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

int main(void){


   int T;
   cin >> T;
   for(int k=0;k<T;k++){
   		cout << "CASE #"<<k+1<<": ";
   		std::cout << std::fixed << std::setprecision(7);
   		double C, F, X, R;
   		cin >> C >> F >> X;
   		R = 2.0;

   		double t1 = X/R;
   		double t2 = C/R;
   		double t3 = X/ (R+F);
   		if(t1 <= t2+t3){
   			cout << t1 <<endl;
   			continue;
   		}
   		else{
   			double t = t2;
   			// cout << t1 <<" " << t2+t3 << " " << R <<endl;
   			R += F;
   			t1 = X/R;
   			t2 = C/R;
   			t3 = X/(R+F);
   			while(t1 > t2+t3){
   				// cout << t1 <<" " << t2+t3 << " " << R <<endl;
   				t += t2;
	   			R += F;
	   			t1 = X/R;
	   			t2 = C/R;
	   			t3 = X/(R+F);
   			}
   			cout << t + t1 << endl;
   		}
   }
   return 0;
}
