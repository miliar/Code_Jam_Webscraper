
#include <iostream>
#include <cstdio>
#include <queue>
#include <algorithm>
#include <cstring>
using namespace std;

#define DBG(X)

bool palin(long long n)

{
  bool is = true;
  char t[20];
  memset(t, 0, sizeof(t));

  int k = 0;  
  while (n > 0)
  {
    t[k] = n % 10;
    k++;
    n /= 10;
  }
  
  for (int i = 0; i < k; i++)
    if (t[i] != t[k - i - 1]) return false;
    
  return true;
  
}


int main()

{
  long long T, A, B;
  //scanf("%d", &T);
  cin >> T;
  for (int z = 1; z <= T; z++)
  {
    //scanf("%d %d", &A, &B);
    cin >> A >> B;
    int ret = 0;
    
    for (long long i = 1; i <= B; i++)
    {
      if (i * i > B) break;
      if (i * i >= A)
        if (palin(i) && palin(i * i))
        {
          //cout << i << " " << i * i << endl;
          ret++;
        }
    }
    
    printf("Case #%d: %d\n", z, ret);
  }  
  
  return 0;
}
