#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

int remainsinrow[100];
int remainsincol[100];
int numinrow[100][100];
int numincol[100][100];
int table[100][100];

int main() {
  int T;
  cin >> T;
  int N, M;
  for (int t = 0; t < T; t++) {
    cout << "Case #" << t+1 << ": ";
    cin >> N >> M;

    for (int i = 0; i < 100; i++) {
      remainsinrow[i] = M;
      remainsincol[i] = N;
      for (int j = 0; j < 100; j++)
	numinrow[i][j] = numincol[i][j] = 0;
    }

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
	int h;
	cin >> h;
	h--;
	numinrow[h][i]++;
	numincol[h][j]++;
	table[i][j] = h;
      }
    }

    for (int h = 0; h < 100; h++) {
      for (int i = 0; i < N; i++) {
	for (int j = 0; j < M; j++) {
	  if (table[i][j] == h) {
	    if (numinrow[h][i] == remainsinrow[i] ||
		numincol[h][j] == remainsincol[j]) {
	    } else {
	      cout << "NO" << endl;
	      goto end;
	    }
	  }
	}
      }

      for (int i = 0; i < N; i++)
	remainsinrow[i] -= numinrow[h][i];
      for (int i = 0; i < M; i++)
	remainsincol[i] -= numincol[h][i];
    }

    cout << "YES" << endl;
  end:
    ;
  }

  return 0;
}
