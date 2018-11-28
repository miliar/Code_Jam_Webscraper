#include <algorithm>
#include <iterator>
#include <iostream>
#include <utility>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;

int main()
{
  int tests;
  
  cin >> tests;
  
  for(int test = 1; test <= tests; test++)
  {
    int A, B, K;
    cin >> A >> B >> K;
    
    ll cnt = 0;
    
    for(int i = 0; i < A; i++)
      for(int j = 0; j < B; j++)
        if( (i & j) < K )
          cnt++;
  
    cout << "Case #" << test << ": " << cnt << endl;
  }
  
	return 0;
}
