#include <iostream>

using namespace std;

long long a[2000];

int main()
{
  int T, N;
  cin >> T;
  for (int t = 1; t <= T; t++)
    {
      cin >> N;
      for (int j = 0; j < N; j++)
	cin >> a[j];
      int l = 0; int r = N - 1;
      int cnt = 0;
      while(l < r)
	{
	  int m = a[l], n = l;
	  for (int j = l; j <= r; j++)
	    if (m > a[j])
	      {
		m = a[j];
		n = j;
	      }
	  if (n - l < r - n)
	    {
	      for (int j = n; j > l; j--)
		swap(a[j], a[j - 1]),cnt++;
	      l++;
	    }
	  else
	    {
	    for (int j = n; j < r; j++)
	      swap(a[j], a[j + 1]),cnt++;
	    r--;
	  }
	}
      cout << "Case #" <<t<<": ";
      cout << cnt << endl;
	  
    }
}
