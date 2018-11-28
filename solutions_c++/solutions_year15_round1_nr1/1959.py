#include <iostream>
using namespace std;

int main()
{
  int T;
  cin >> T;
  
  int One, Two, N, M[1024], Speed;
  for(int t = 1; t <= T; ++t)
  {
    One = 0, Two = 0, N, M[1024], Speed = 0;
    
    cin >> N;
    for(int i = 0; i < N; ++i)
    {
      cin >> M[i];
      
      if(i == 0)
        continue;
        
      if(M[i - 1] - M[i] > 0)
        One += M[i - 1] - M[i];
        
      if(M[i - 1] - M[i] > Speed)
        Speed = M[i - 1] - M[i];
    }
    
    for(int i = 0; i < N - 1; ++i)
      Two += (M[i] < Speed ? M[i] : Speed);
    
    cout << "Case #" << t << ": " << One << " " << Two << endl;
  }
    
  return 0;
}
