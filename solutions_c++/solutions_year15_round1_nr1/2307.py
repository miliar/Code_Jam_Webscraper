#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <functional>

using namespace std;

int main()
{
  int N;
  cin >> N;
  getchar();

  for (int n = 0; n < N; ++n)
  {
    int M, 
      m1 = 0, 
      m2 = 0, 
      *mi;
    cin >> M;
    mi = new int[M];
    m1 = 0;
    m2 = 0;
    for (int i = 0; i < M; ++i) {
      cin >> mi[i];
    }
    
    int cur = mi[0];
    for (int i = 1; i < M; ++i)
    {
      if (mi[i] < cur) {
        m1 += cur - mi[i];
        if ((cur - mi[i]) > m2)
          m2 = cur - mi[i];
      }
      cur = mi[i];
    }

    int no = 0;
    cur = mi[0];
    for (int i = 0; i < M-1; ++i) {
      if (mi[i] < m2)
        no += m2 - mi[i];
    }
    if (m1 <= 0)
      m2 = 0;
    else {
      m2 = m2 * (M-1) - no;
    }

    cout << "Case #" << n + 1 << ": " << m1 << ' ' << m2;
    cout << endl;
    delete[] mi;
  }
  return 0;
}