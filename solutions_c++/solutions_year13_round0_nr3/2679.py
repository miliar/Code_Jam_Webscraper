#include <iostream> //Standard input/output
#include <fstream> //File input/output
#include <cstdlib> //C library
#include <cmath> //Math library
#include <algorithm> //Some algorithms like sorting
#include <vector> //Vectors (Array lists)
#include <string> //Strings

using namespace std; //Used the standard class

ifstream fin ("fair.in");
ofstream fout ("fair.out");

bool palindrome(int num){
   int cache = num;
   int back = 0;
   while (num > 0)
   {
      back = back*10 + num % 10;
      num/=10;
   }
   return cache==back;
}
int main ()
{
   int T;
   fin >> T;
   for(int cas = 1; cas<=T; cas++){
      int A,B;
      fin >> A >> B;
      int count = 0;
      for(int i = 1; i<=1000; i++){
         int sq = i*i;
         if(sq<A) 
            continue;
         if(sq>B) 
            break;
         if(palindrome(i) && palindrome(sq)) count++;
      }
               fout << "Case #" << cas << ": " << count << "\n"; 
   }
   return 0;
}