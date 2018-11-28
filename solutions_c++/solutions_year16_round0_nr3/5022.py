#include<iostream>
#include <fstream>

using namespace std;

int main(){
   long long N,L,T;
   ifstream cf ("coin16.cache");
   cin >> T;
   for(long long t=1;t<=T;++t){
      cin >> N;
      cin >> L;
      string line;
      cout << "Case #"<<t<<":"<<endl;
      for(long long i=0;i<L;++i){
         getline (cf,line);
         cout << line <<endl;
      }
   }
   cf.close();
   
}
