//codejam4easy

#include <iostream>

using namespace std;

int main()
{
  int size;
  int K, C, S;
  cin >> size;
  for(int i =0 ; i< size; i++)
  {
    cin >> K >> C >> S;
    cout << "Case #" << i+1 << ": ";
    cout << "1";
    for(int j = 2; j <= K;j++)
      cout << " " << j;
    cout << "\n";
  }
  return  0;
}
