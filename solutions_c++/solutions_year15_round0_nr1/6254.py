#include <iostream>
using namespace std;

int main (){
   int T;
   cin>>T;
   for (int caseN=1;caseN<=T;caseN++){
      int smax;
      string sk;
      cin>>smax>>sk;
      int total = 0;
      int added = 0;
      for (int s=0;s<=smax;s++){
         int k = sk[s] - '0';
         if (k > 0 && s > total){
            added += s - total;
            total = s;
         }
         total += k;
      }
      cout<<"Case #"<<caseN<<": "<<added<<endl;
   }
   
}
