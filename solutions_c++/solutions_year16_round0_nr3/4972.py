#include <iostream>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <iomanip>
#include <sstream>

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

using namespace std;

string num(100, '0');

int list[11] = {0};
int c = 0;
bool add(int n)
{
  int i = n;
  while(i >= 0)
  {
    if(num[i] == '0')
    {
      num[i] = '1';
      return true;
    }
    else
    {
      num[i] = '0';
    }
    i--;
  }

  return false;
}

bool check()
{
  long long a;
  int times = 0;
  for(int i = 2; i <= 10; i++ )
  {
 
    a = stol(num,nullptr, i);
  
    long long upper = sqrt(a);
    for(long long j = 2; j <= upper; j++)
    {
      if (a % j == 0)
      {
          list[i] = j;
          times++;
            break;
      }  
      
    }
  }
  if (times == 9)
    return true;

  return false;

}
int main()
{
  int T;
  cin >> T;
  int N, J;
  cin >> N >> J;
  num.resize(N);
  for(int i = 0; i < N; i++)
    num[i] = '0';
  for(int t = 1; t <= T; t++)
  {
  	cout << "Case #"<<t << ": \n";
    num[0] = '1';
    num[N-1] = '1';
    bool status = 1;
    while(status && c < J)
    {
      if(check() )
      {
        cout << num <<" ";
        for(int i = 2; i <= 10; i++)
          cout << list[i] << " ";
        cout << endl;
        c++;
      }
      status = add(N-1);
      while(num[N-1] != '1' && status)
        status = add(N-1);

    }

  }


  return 0;
}