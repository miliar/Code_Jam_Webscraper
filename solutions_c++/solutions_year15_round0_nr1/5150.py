#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main()
{
  ifstream fin( "A-large.in.txt" );
  ofstream fout( "output" );
  cin.rdbuf( fin.rdbuf() );
  cout.rdbuf( fout.rdbuf() );

  int num, max_s;
  string aud;
  
  cin >> num;

  int ca = 1;
  while ( cin >> max_s >> aud ) {
    cout << "Case #" << ca
	 << ": ";
    int a2add = 0, as = 0;;
    for ( int i = 0; i <= max_s; i++ ) {
      if ( as >= i )
	as += aud[ i ] - '0';
      else {
	a2add += i - as;
	as = i + aud[ i ] - '0';
      }
    }
    cout << a2add << endl;
    ca++;
  }

  return 0;
}
