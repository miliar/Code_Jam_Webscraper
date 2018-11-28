#include <iostream> //Standard input/output
#include <fstream> //File input/output
#include <cstdlib> //C library
#include <cmath> //Math library
#include <algorithm> //Some algorithms like sorting
#include <vector> //Vectors (Array lists)
#include <string> //Strings
#include<map>

using namespace std; //Used the standard class

ifstream fin ("lawnmower.in");
ofstream fout ("lawnmower.out");
//#define fout cout
int main ()
{
   int T;
   fin >> T;
   for(int cas = 1; cas<=T; cas++){
      int N,M;
      fin >> N >> M;
      int board[N*M];
      for(int i = 0; i<N*M; i++){
         fin >> board[i];
      }
      bool possible = true;
      for(int i = 0; possible && i<N; i++){
         for(int j = 0; possible && j<M;j++){
            //cout << board[i*M+j] << " ";
            bool works = true;
            for(int i2 = 0; works && i2<N;i2++){
               if(board[i2*M+j]>board[i*M+j]) works = false;
            }
            if(works) 
               continue;
            works = true;
         
            works = true;
            for(int i2 = 0; works && i2<M;i2++){
            //cout << "|" << board[i*M+i2] << "|";
               if(board[i*M+i2]>board[i*M+j]) works = false;
            }
            if(!works) possible = false;
         }
         //cout << endl;
      }
      fout << "Case #" << cas << ": ";
      if(possible) fout << "YES\n";
      else fout << "NO\n";
   }
   return 0;
}