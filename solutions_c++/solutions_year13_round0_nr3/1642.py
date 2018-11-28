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

string reverse( string s ){
  forn( i, s.length()/2 )
    swap( s[i], s[s.length()-1-i] );
  return s;
}
string ll2string( long long n ){
  stringstream ss;
  ss << "";
  ss << n;
  //cout << ss.str() ENDL;
  return ss.str();
}
long long radix4( long long n ){
  //return n;
  if(n==0)
    return 0;
  long long ret=radix4(n/4)*10 + n%4;
  
  //cout << n COMMA ret ENDL;
  return ret;
}

vector<long long> list;
void makelist( long long min, long long max){
  long long i=0;
  long long j=0;
  //long long i=(long long)sqrt(min)-1;
  long long i2=i*i;
  while( i2<=max ){
    if( i2<min ){
      j++;
      i=radix4(j);
      i2=i*i;
      continue;
    }
    
    string tmp=ll2string(i);
    if( reverse(tmp)==tmp ){
      string tmp2=ll2string(i2);
      if( reverse(tmp2)==tmp2 ){
	//cout << i2 << " is true " << i  ENDL;
	//ret++;
	
	list.push_back(i2);
      }
      //else
      //cout << i2 << " isnot true " << i  ENDL;
    }
    
    j++;
    i=radix4(j);
    i2=i*i;
  }
}

int sub1(){
  int ret=0;
  long long min;
  long long max;
  cin >> min;
  cin >> max;
  //cout << min COMMA max ENDL;
  
  fore( i, list )
    if( min<=list[i] && list[i]<=max )
      ret++;
  
  return ret;
}


int main (int argc, char*argv[]){
  int T;
  cin >> T;
  
  makelist( 1, (long long)1000000000000000LL );
  
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
