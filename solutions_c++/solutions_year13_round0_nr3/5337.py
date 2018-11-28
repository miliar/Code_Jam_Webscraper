#include <iostream>
#include <vector>
#include <iterator>
#include <string>
#include <cmath>
#include <cstdlib>

using namespace std;

bool is_fair(int x)
{
  int value;
  int v_size;
  vector<int> v_int;
  
  value = x;

  while(value > 0) {
    v_int.push_back(value % 10);
    value /= 10;
  }

  v_size = v_int.size();
  for(int i = 0; i < v_size / 2; i++) {
    if(v_int[i] != v_int[v_size - 1 - i]) {
      return false;
    }
  }

  return true;
}

bool is_square(int x)
{
  double mod;

  mod = fmod(sqrt(x), 1);

  return mod == 0;
}

int main(void)
{
  int i_size;
  int ctr;
  int domain[2];

  cin >> i_size;

  for(int i = 0; i < i_size; i++) {
    ctr = 0;
    cin >> domain[0] >> domain[1];
    cout << "Case #" << (i + 1) << ": ";
    for(int j = domain[0]; j <= domain[1]; j++) {
      if(is_square(j)) {
	if(is_fair(j)) {
	  if(is_fair(sqrt(j))) {
	    ctr++;
	  }
  	}
      }
    }
    cout << ctr << endl;
  }
 
  return 0;
}
