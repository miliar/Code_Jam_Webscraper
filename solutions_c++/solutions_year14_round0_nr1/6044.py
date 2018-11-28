#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <cstdio> 
 
using namespace std;
 
vector <pair<int, int>> graf[100001];
 
int N, M, a, b, ans, n, i, j, q, val, arr[5][5], arr2[5][5];

 
int main()
{
  #pragma comment(linker, "/STACK:64000000")
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> n;
  for (i = 0; i < n; i++)
  {
	cin >> a;
	a--;
	ans = 0;
	val = 0;
	for (j = 0; j < 4; j++)
	  for (q = 0; q < 4; q++)
		cin >> arr[j][q];
	cin >> b;
	b--;
	for (j = 0; j < 4; j++)
	  for (q = 0; q < 4; q++)
		cin >> arr2[j][q];
	for (j = 0; j < 4; j++)
	  for (q = 0; q < 4; q++)
	  if (arr[a][j] == arr2[b][q])
	  {
		ans++;
		val = arr[a][j];
	  }
	cout << "Case #" << i + 1 << ": ";
	if (ans == 0)
	  cout << "Volunteer cheated!" << endl;
	if (ans == 1)
	  cout << val << endl;
	if (ans > 1)
	  cout << "Bad magician!" << endl;
  }
}