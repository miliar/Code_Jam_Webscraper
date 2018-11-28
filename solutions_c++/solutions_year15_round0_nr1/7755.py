#include <iostream>
#include <fstream>
#include <string>

using namespace std;



int main()
{
   int nCases;
   ifstream input ("A-large.in");
   ofstream output ("output");
   input>>nCases;

   for(int i=1; i<=nCases; i++){
      int maxShyness;
      input>>maxShyness;

      string data;
      getline(input, data);

      data.erase(0,1);

      int sum = 0;
      int add = 0;
      for(int i=0; i<data.length(); i++){
         int currentData = (int)data[i]-'0';
         while(sum+add < i){
            add++;
         }
         sum+=currentData;
      }

      while(sum+add<maxShyness){
         add++;
      }

      output<<"Case #"<<i<<": "<<add<<endl;

   }

   return 0;
}
