#include <iostream>
#include <algorithm>

using namespace std;

int inv(int A[], int n)
{
  int c = 0;
  for (int i = 0; i < n; i++) {
    for (int j = i+1; j < n; j++) {
      c += (A[i] > A[j]);
    }
  }
  return c;
}

void solve()
{
  int N;
  int A[1000];

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }

  int s = 0, e = N;
  int swaps = 0;
  for (int i = 0; i < N; i++) {
    int mini = min_element(A+s, A+e) - A;
    int move_left = mini - s;
    int move_right = e - mini - 1;
    if (move_left <= move_right) {
      while (mini < e - 1) {
	swap(A[mini], A[mini+1]);
	mini++;
      }
      e--;
    } else {
      while (mini-1 >= s) {
	swap(A[mini-1], A[mini]);
	mini--;
      }
      s++;
    }
    swaps += min(move_left, move_right);
  }
  cout << swaps << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
