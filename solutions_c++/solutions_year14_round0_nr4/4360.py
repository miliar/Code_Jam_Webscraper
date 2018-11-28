#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int I = 0; I < T; I++) {
    int N;
    cin >> N;
    double a[N], b[N];
    for (int i = 0; i < N; i++) {
      cin >> a[i];
    }
    sort(a, a + N, greater<double>());
    for (int i = 0; i < N; i++) {
      cin >> b[i];
    }
    sort(b, b + N, greater<double>());
    int j = 0;
    int c = 0;
    for (int i = 0; i < N; i++) {
      if (a[i] > b[j]) {
	c++;
      } else {
	j++;
      }
    }
    sort(a, a + N);
    int score = 0;
    int begin = 0;
    int end = N - 1;
    for (int i = 0; i < N; i++) {
      if (a[i] < b[end]) {
	begin++;
      } else {
	score++;
	end--;
      }
    }
    cout << "Case #" << I + 1 << ": " << score << " " << c << endl;
  }
}
