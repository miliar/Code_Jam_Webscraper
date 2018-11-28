#include <iostream>
#include <cmath>
#include <string>
#include <sstream>

using namespace std;

string Int2String(int num){
  stringstream ss;
  ss << num;
  return ss.str();
}

bool Palindromic( string s ){
  int i = 0;
  int j = s.size() - 1;
  
  while( s[i] == s[j] ) {
	++i;
	--j;
  }
  if(i > j)
	return true;
  else
	return false;

}

int main( void ) {

  int T;

  cin >> T;

  for ( int i=1; i<=T; ++i ) {
	int A, B;
	int cnt = 0;

	cin >> A >> B;

	for( int j=A; j<=B; ++j ){
	  int square = (int)sqrt(j);

	  if (j != (square*square) )
		  continue;

	  string str = Int2String( j );
	  if( Palindromic(str) ){

		int sqr = sqrt((double)j);
		str = Int2String(sqr);
		if( Palindromic(str) )
			++cnt;
	  }
	  /*
	  if (j == (double)(square*square) ) {

		string str, str_inv;

		str = Int2String( j );

		if( Palindromic(str) )
		  ++cnt;
	  }
	  */

	}

	cout << "Case #" << i << ": " << cnt << endl;
  }

  return 0;

}
