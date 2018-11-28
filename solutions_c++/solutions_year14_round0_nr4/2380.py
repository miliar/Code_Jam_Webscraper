#include <string>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath> 

using namespace std;


int main() {

   //num of test cases
   int test_cnt;
   
   cin >> test_cnt;

   for(int idx = 1; idx <= test_cnt; idx++) {
      int N = 0;
      int y = 0;
      int z = 0;

      vector<double> Naomi;
      vector<double> Ken;
      
      cin >> N;
      for(int i = 0; i < N; i++) {
         double tmp;
         cin >> tmp;
         Naomi.push_back(tmp);
      } 
      for(int i = 0; i < N; i++) {
         double tmp;
         cin >> tmp;
         Ken.push_back(tmp);
      } 
 
      sort(Ken.begin(), Ken.end());
      sort(Naomi.begin(), Naomi.end());

      vector<double> Ken_tmp = Ken;
      vector<double> Naomi_tmp = Naomi;

      // play deceipt war.
      while(!Naomi_tmp.empty()){
         if(Naomi_tmp.back() > Ken_tmp.back()){
            y++;  
            Naomi_tmp.pop_back();
            Ken_tmp.pop_back();
         }
         else{
            Naomi_tmp.erase(Naomi_tmp.begin());
            Ken_tmp.pop_back();
         }
      }

      // play war.
      for(int i = 0; i < N; i++) {
         for(int j = 0; j < Ken.size(); j++) {
            if(Ken[j] > Naomi[i]) {
               Ken.erase(Ken.begin()+j);
               break;
            }  
         }
      } 
     
      z = Ken.size();
      cout << "Case #" << idx << ": " << y << " " << z << endl;
     
      Ken.clear(); Naomi.clear();
      
   }

   return 0;
}
