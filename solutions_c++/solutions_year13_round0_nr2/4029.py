#include <cstdio>
#include <iostream>
#include <istream>
#include <ostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <iomanip>
#include <sstream>
#include <fstream>

using namespace std;

short field[100][100];
short testfield[100][100];
short mn[100];
short mm[100];

ofstream outfile;

void getmax(short n, short m){
     for (short i = 0; i < n; i++){
                   mm[i] = 0;
         for(short j = 0; j < m; j++){
                   if (field[i][j] > mm[i])
                   mm[i] = field[i][j];
                   }
                   }
     for (short i = 0; i < m; i++){
                   mn[i] = 0;
         for(short j = 0; j < n; j++){
                   if (field[j][i] > mn[i])
                   mn[i] = field[j][i];
                   }
                   }
         }

void maketest(short n, short m){
     for( short i = 0; i < n; i++){
          for ( short j = 0; j < m; j++){
              testfield[i][j] = mm[i];
              }
          }
     for (short i = 0; i < m; i++){
         for ( short j = 0; j < n; j++){
             if(testfield[j][i]> mn[i])
             testfield[j][i] = mn[i];
             }
         }
}

void comparefields(short n, short m){
         for(short i = 0; i < n; i++){
                   for (short j = 0; j < m; j++){
                       if(field[i][j] != testfield[i][j]){
                                      outfile<<"NO"<<endl;
                                      return;
                                      }
                                      }
                                      }
                       outfile<<"YES"<<endl;
                       return;
                       }


int main () {
  string line;
  ifstream myfile;
  myfile.open("exampleB.txt");
  outfile.open("outputB.txt");
  short t;
  short n,m;
  myfile >> t;
  getline(myfile,line);
  for(short i = 0; i < t; i++){
          myfile >> n >> m;
          getline(myfile,line);
          for (short j = 0; j < n; j++){
              for (short k = 0; k < m; k++)
                  myfile>>field[j][k];
              getline(myfile,line);
              }
              outfile<<"Case #"<<i+1<<": ";
          getmax(n,m);
          maketest(n,m);
          comparefields(n,m);
          /*for ( int j = 0; j< n; j++){
               for ( int k = 0; k < m; k++)
               cout << field[j][k]<<" ";
              
              cout <<endl;
          }*/
          }
    outfile.close();                
    myfile.close();
  system("pause");
  return 0;
}
