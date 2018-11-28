#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
vector<long long int> fractile_small(int K, int C);
int main(){
  fstream fin, fout;
  fin.open("D-small-attempt3.bin");
  fout.open("output.out");
  if (!fin.is_open()) {
    //cout << "in file was not open" << endl;
  }
  if (!fout.is_open()) {
    //cout << "out file was not open" << endl;
  }
  int test_num;
  fin >>  test_num;
  //cout << "this is test number = " << test_num << endl;
 for (int i = 0; i < test_num; i++) {
   int K,C,S;
   fin >> K;// //cout << "this is K = " <<  K << endl;
   fin >> C; //cout << "this is C = " << C << endl;
   fin >> S;// //cout << "this is S = " << S << endl;
   fout << "Case #" << i+1 << ": ";
   vector<long long int> result = fractile_small(K,C);
   int len = result.size();
   if (len > S) {
     fout << "IMPOSSIBLE" << endl;
   }
   else{
     for (int i = 0; i < len-1; i++) {
       fout << result[i]+1 << " ";
     }
     fout << result[len-1]+1 << endl;
   }
 }
   fin.close();
   fout.close();
   return 0;

}
 vector<long long int> fractile_small(int K, int C)
 {
   vector<long long int> result;
   // K: length, C:tile, S: small S = K
   if (C == 1){
     for (int i = 0; i < K; i++) {
       result.push_back(i);
     }
   }
   else if( K > C ){
     for (int i = 0; i <= K-C; i++){
       long long int pos = i;
       for (int level = 2; level <= C; level++) {
         pos = pos*K + i+level-1; 
       }
       result.push_back(pos);
     }
   }
   else if( K <= C){
     long long int pos = 0;
     for (int level = 2; level <= C; level++) {
       if (level <= K) pos = pos*K + level-1;
       else pos = pos*K + K-1;
     }
     result.push_back(pos);
   }
   return result;
 }
