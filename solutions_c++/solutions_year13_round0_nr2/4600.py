#include <iostream>
#include <cstring>
using namespace std;

int main(int argc, char** argv)
{
  unsigned v[100][100];

  unsigned t;
  cin >> t;

  for(int k = 1; k <= t; k++)
    {
      unsigned n, m;
      cin >> n >> m;

      unsigned l[n], c[m];
      bzero(l, n * sizeof(unsigned));
      bzero(c, m * sizeof(unsigned));

      for(int i = 0; i < n; i++)
	for(int j = 0; j < m; j++)
	  {
	    unsigned h;
	    cin >> h;

	    v[i][j] = h;

	    if(l[i] < h)
	      l[i] = h;

	    if(c[j] < h)
	      c[j] = h;
	  }

      bool possible = true;
      for(int i = 0; possible && i < n; i++)
	for(int j = 0; possible && j < m; j++)
	  if(v[i][j] < l[i] && v[i][j] < c[j])
	    possible = false;

      cout << "Case #" << k << ": " << (possible ? "YES" : "NO") << endl;
    }

  return 0;
}
