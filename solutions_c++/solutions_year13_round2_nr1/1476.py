#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>

using namespace std;

int _t;
int n, in[105], result;
long long a;

int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  cin >> _t;
  for (int t = 1; t <= _t; t++) {
    result = 0;
    cin >> a >> n;
	  for (int i = 0; i < n; i++) scanf("%d", &in[i]);
	  sort(in, in + n);
	  for (int i = 0; i < n; i++) {
		  if (a > in[i]) {
			  a += in[i];
		  } else {
        int j = 0;
        for (j = 0; j < n - i; j++) {
          result++;
          a += a - 1;
          if (a > in[i]) {
            a += in[i];
            break;
          }
        }
        if (j == n - i) {
          break;
        }
      }
	  }
	  cout << "Case #" << t << ": " << min(result, n) << endl;
  }
  return 0;
}