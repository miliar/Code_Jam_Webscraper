#include <iostream>
using namespace std;

int main()
{  
  int T, Case = 1;
  cin >> T;
  
  int X, R, C;
  for(int t = 0; t < T; ++t)
  {
    cin >> X >> R >> C;
    bool Gabriel;
    
    if(X >= 7 || (X > R && X > C) || X > R * C || (R * C) % X != 0)
      Gabriel = false;
    else if(X <= 2)
      Gabriel = true;
    else if((X + 1) / 2 >= C || (X + 1) / 2 >= R)
      Gabriel = false;
    else
      Gabriel = true;
    
    if(Gabriel)
      cout << "Case #" << Case++ << ": GABRIEL" << endl;
    else
      cout << "Case #" << Case++ << ": RICHARD" << endl;
  }
    
  return 0;
}
