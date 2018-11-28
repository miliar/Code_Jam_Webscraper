#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>
#include <algorithm>
#include <math.h>
#define fore(I,D) for(unsigned int(I)=0;(I)<(D).size();++(I))
#define forn(I,S) for(unsigned int(I)=0;(I)<(S);++(I))
#define ALL(C) (C).begin(),(C).end()
#define COUNT(C,N) count(ALL(C),(N))
#define SORT(C) sort(ALL(C))
#define REV(C) reverse(ALL(C))
#define UNIQ(C) (C).erase( unique(ALL(C)), (C).end());
#define FIND(C,N) find(ALL(C),N)
#define FILL(C,N) fill(ALL(C),N)
#define REPLACE(C,N1,N2) replace(ALL(C),N1,N2)
#define COMMA <<","<<
#define ENDL <<endl
//#include <iomanip>
using namespace std;
// time g++ -Wall -O2 -mtune=pentium-m qualb.cpp ; time cat sample.in | ./a.exe | tee out


int sub1(){
  int ret=0;
  long long r;
  double t;
  cin >> r;
  cin >> t;
  //cout << "r,t=" << r COMMA t ENDL;
  
  //double a=( (double)(r+1)*(r+1) - (double)r*r );
  double a= 2*r + 1;
  
  double x= ( (2-a) + sqrt( (a-2)*(a-2) + 8*t ) )/4;
  //cout << "a,x=" << a COMMA x ENDL;
  
  ret=x;
  
  return ret;
}


int main (int argc, char*argv[]){
  int T;
  cin >> T;
  
  //cout << T ENDL;
  for ( int i=0 ; i<T ; i++ ){
    cout << "Case #" << i+1 << ": " ;

    cout << sub1();
    //cout.precision(6);
    //cout << sub1();
    //printf("%6f",sub1());
    cout << endl;
  }
  
  return 1;
};
