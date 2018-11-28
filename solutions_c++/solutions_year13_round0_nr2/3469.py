#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

int main(int argc, char *argv[])
{
  ifstream fin("B-large.in.txt");
  // ifstream fin("B.in.txt");
  int cases;
  int cnt = 0;

  fin >> cases;
  while (++cnt <= cases) {
    int n, m;
    fin >> n >> m;

    int **p;
    p = new int*[n+1];
    for (int i = 0; i < n+1; ++i)
      p[i] = new int[m+1];
    for (int i = 0; i < n+1; ++i)
      for (int j = 0; j < m+1; ++j)
	p[i][j] = 0;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j)
	fin >> p[i][j];

    for (int i = 0; i < n; ++i) {
      int max = p[i][0];
      for (int j = 1; j < m; ++j)
	if (p[i][j] > max)
	  max = p[i][j];
      p[i][m] = max;
    }
    for (int i = 0; i < m; ++i) {
      int max = p[0][i];
      for (int j = 1; j < n; ++j)
    	if (p[j][i] > max)
    	  max = p[j][i];
      p[n][i] = max;
    }

    int poss;
    for (int i = 0; i < n; ++i) {
      poss = true;
      for (int j = 0; j < m; ++j) {
	if ((p[i][j] > p[i][m] && p[i][j] > p[n][j]) ||
	    (p[i][j] < p[i][m] && p[i][j] < p[n][j])) {
	  poss = false;
	  break;
	}
      }
      if (! poss)
	break;
    }

    cout << "Case #" << cnt << ": " << (poss ? "YES" : "NO") << endl;    
    // cout << "Case #" << cnt << ": " << n << ' ' << m << ' ' << (poss ? "YES" : "NO") << endl;
    // for (int i = 0; i < n+1; ++i) {
    //   for (int j = 0; j < m+1; ++j)
    // 	cout << p[i][j] << ' ';
    //   cout << endl;
    // }

    for (int i = 0; i < n+1; ++i) {
      delete []p[i];
      p[i] = NULL;
    }
    delete []p;
    p = NULL;
  }
  fin.close();
  return 0;
}
