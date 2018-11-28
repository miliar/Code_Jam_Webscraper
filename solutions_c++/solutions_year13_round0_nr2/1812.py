#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>
#include <algorithm>
#include <math.h>
#define fore(I,D) for(int(I)=0;(I)<(D).size();++(I))
#define forn(I,S) for(int(I)=0;(I)<(S);++(I))
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


string sub1(){
  int xsize,ysize;  
  cin >> ysize;
  cin >> xsize;
  //cout << min COMMA max ENDL;
  
  int area[xsize+1][ysize+1];
  
  forn( y, ysize )
    forn( x, xsize )
    cin >> area[x][y];
  
  int x_maxh[xsize+1];
  forn( x, xsize ){
    x_maxh[x]=-1;
    forn( y, ysize )
      x_maxh[x]=max(x_maxh[x], area[x][y] );
  }
  
  int y_maxh[ysize+1];
  forn( y, ysize ){
    y_maxh[y]=-1;
    forn( x, xsize )
      y_maxh[y]=max(y_maxh[y], area[x][y] );
  }
  
  forn( y, ysize )
    forn( x, xsize )
    if( area[x][y]<x_maxh[x] && area[x][y]<y_maxh[y] )
      return "NO";
  
  return "YES";
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
