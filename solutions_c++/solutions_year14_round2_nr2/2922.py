#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<string>
#include<cstring>

using namespace std;

int main()
{
  freopen("ask.in", "r", stdin);
  freopen("ans.out", "w", stdout);

  int t;
	cin >> t;
  for (int i = 0; i < t; i++)
  {
    int a, b, k;
    int ans = 0;
    cin >> a >> b >> k;
    for (int l = 0; l < a; l++)
      for (int j = 0; j < b; j++)
      {
      //  cout << l << " " << j << " " << l&j << endl; 
        if ((l&j) < k)
          ans++;
      }
    cout << "Case #" << i + 1 << ": "<< ans << endl;
  }

  return 0;
}

