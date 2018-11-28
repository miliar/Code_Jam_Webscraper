#include <iostream>

using namespace std;


int T;
int seed;
bool flags[10];


bool all_flags()
{
  for (int k=0; k<10; k++) 
    if( flags[k] == false ) return false;
  return true;
}

void set_flags(int x)
{
  while ( x > 0 ) {
    int d = x % 10;
    flags[d] = true;
    x = x / 10;
  }
}


int main(){

  cin >> T;
  cerr << T << " test cases" << endl; 

  for(int ii = 1; ii<=T; ii++){
    cin >> seed;
    cerr << ". " << seed << endl;
    
    for (int k=0; k<10; k++) 
      flags[k] = false;

    if ( seed == 0 ){
      cout << "Case #" << ii << ": INSOMNIA" << endl;
    }
    else {
      int n = seed;
      set_flags(n);	
      while ( !all_flags() ) {
	// cerr << n << endl;
	n += seed;
	set_flags(n);
      }
      cout << "Case #" << ii << ": " << n << endl;
    }

  }
  return 0;
}

