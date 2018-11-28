#include <iostream>
#include <cstdlib>

using namespace std;

typedef long long BigInt;

int main()
{
  BigInt T, K, C, S;
  
  cin >> T;
  
  for (BigInt c=1;c<=T;c++){
      cin >> K >> C >> S;
      cout << "Case #" << c << ": ";
      for (BigInt i=1;i<=S;i++) cout << i << " ";
      cout << endl;    
  }
    
}
