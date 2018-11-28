#include <iostream>
#include <cstdlib>
#include <map>
#include <set>

using namespace std;

int main(){
  int aux;
  int T, N;
  set<int> s;

  cin >> T;
  for( int i = 0; i < T; i++){
    cin >> N;
    cout << "Case #" << i+1 << ": ";
    if( N == 0 ){
      cout << "INSOMNIA" << endl;
      continue;
    }
    s.clear();
    for( int i = 1; i < 100; i++ ){
      aux = i*N;
      do{
	s.insert( aux%10 );
	aux /=10;
      } while( aux );
      if( s.size() == 10 ){
	cout << i*N << endl;
	break;
      }
    }
    if( s.size() != 10 ) cout << "INSOMNIA" << endl;
  }
  return 0;
}
