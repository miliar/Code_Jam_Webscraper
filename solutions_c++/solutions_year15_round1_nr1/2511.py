

#include<iostream>
using namespace std;

int main() {
  int cases,i=0,elem,list[10000],firstMethod,rate,secondMethod,consumed=0;
  cin >> cases;
  while( i<cases ) {
    cin >> elem >> list[0] ;
    firstMethod=0;
    secondMethod=0;
    rate=0;
    for( int j=1 ;j< elem; j++ ) {
      cin >> list[j];
      consumed = list[ j-1 ] - list[j];
      if( consumed >= 0 ) {
	firstMethod += consumed;
	if ( rate < consumed )
	  rate = consumed;
      }
    }
    for(int j=0; j<elem-1; j++)
	secondMethod+= ( list[j] <= rate )? list[j]:rate;
    cout << "Case #" << ++i << ": " << firstMethod << " " <<secondMethod << endl;
  }
  return 0;
}
