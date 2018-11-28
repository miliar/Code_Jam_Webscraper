#include <iostream>
using namespace std;

int main()
{
  int T, Case = 1;
  cin >> T;
  
  int D, P[1024];
  for(int t = 0; t < T; ++t)
  {
    for(int i = 0; i < 1024; ++i)
      P[i] = 0;
          
    cin >> D;
    
    int temp, max = 0;
    for(int i = 0; i < D; ++i)
    {
      cin >> temp;
      
      ++P[temp];
      
      if(temp > max)
        max = temp;
    }
      
    int min = max;
    for(int i = 1; i < max; ++i)
    {
      int use = i;
      for(int j = i + 1; j <= max; ++j)
        use += (j % i == 0 ? j / i - 1 : j / i) * P[j];
        
      if(use < min)
        min = use;
    }
    
    cout << "Case #" << Case++ << ": " << min << endl;
  }
    
  return 0;
}
