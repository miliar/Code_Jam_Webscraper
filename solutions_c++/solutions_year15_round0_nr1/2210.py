#include <string>
#include <fstream>
#include <iostream>
using namespace std;

int main()
{
  ifstream fin("");
  ofstream fout("A-small.out");
    
  int T, Case = 1;
  cin >> T;
  
  int M, S[1024];
  string str;
  for(int t = 0; t < T; ++t)
  {
    cin >> M >> str;
    for(int i = 0; i <= M; ++i)
      S[i] = str.at(i) - '0';
      
    int ans = 0, sum = 0;
    for(int i = 0; i <= M; ++i)
    {
      if(sum < i)
      {
        ans += i - sum;
        sum += i - sum;
      }
      
      sum += S[i];
    }
    
    cout << "Case #" << Case++ << ": " << ans << endl;
  }
    
  return 0;
}
