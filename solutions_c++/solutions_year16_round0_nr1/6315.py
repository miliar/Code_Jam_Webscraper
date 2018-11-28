#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <string>
#include <queue>
using namespace std;
typedef long long ll;
typedef pair<int, int> P;

bool a[10];
int f;

bool check(int n){
  while( n != 0 ){
    int k = n % 10;
    if( !a[k] ){
      f++;
      a[k] = true;
      if( f == 10 )
	return true;
    }
    n /= 10;
  }
  return false;
}
int main(){
  int T, N;
  cin >> T;
  for(int c = 1; c <= T; c++){
    cin >> N;
    if( N == 0 ){
      cout << "Case #" << c << ": INSOMNIA" << endl;
      continue;
    }
    f = 0;
    fill( a, a + 10, false );
    int i;
    for(i = 1; ; i++){
      if( check( i * N ) )
	break;
    }
    cout << "Case #" << c << ": " << i * N << endl;
  }
}
