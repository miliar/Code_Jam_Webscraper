#include<iostream>
using namespace std;

int main()
{
  int A, B, K, T;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
    int count = 0;
    cin >> A >> B >> K;
    for(int k = 0; k < K; k++)
    {
      for(int a = 0; a < A; a++)
        for(int b = 0; b < B; b++)
          if(k == (a&b)) ++count;
    }
    cout << "Case #" << t << ": " << count << endl;
  }
  return 0;
}
