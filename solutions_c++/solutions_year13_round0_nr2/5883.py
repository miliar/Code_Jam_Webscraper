#include <cstdio>
#include <iostream>

using namespace std;

int a[110][110];
int maxrow[110];
int maxcol[110];

int main() {

  int ntests;
  cin >> ntests;

  for (int test = 1; test <= ntests; test++) {
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
	cin >> a[i][j];
      }
    }

    for (int i = 0; i < n; i++)
      maxrow[i] = a[i][0];
    for (int j = 0; j < m; j++)
      maxcol[j] = a[0][j];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
	maxrow[i] = max(maxrow[i], a[i][j]);
	maxcol[j] = max(maxcol[j], a[i][j]);
      }
    }

    bool good = true;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
	if (a[i][j] < maxrow[i] && a[i][j] < maxcol[j])
	  good = false;
      } 
    }

    cout << "Case #" << test << ": ";
    if (good)
      cout << "YES\n";
    else
      cout << "NO\n";
  }



  return 0;
}

