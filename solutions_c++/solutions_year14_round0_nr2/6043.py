#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <cstdio> 
 
using namespace std;
  
int n, i;
double C, F, X, Gr, ans, loc_ans, T, j;

 
int main()
{
  #pragma comment(linker, "/STACK:64000000")
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> n;
  for (i = 0; i < n; i++)
  {
	cin >> C >> F >> X;
	Gr = 2;
	ans = 1000000000;
	T = 0;

	for (j = 0; j < 10000000; j++)
	{
	  loc_ans = T + X / Gr;
	  T += C / Gr;
	  ans = min(ans, loc_ans);
	  Gr += F;
	}
	cout << "Case #" << i + 1 << ": ";
	printf("%.10f", ans);
	cout<<endl;
  }
}