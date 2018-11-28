#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>


using namespace std;

int i2num[64][3];
double prod2prob[64][126];
double prob[64];

int main() {

  int index = 0;
  for (int a = 2; a <= 5; a++) {
    for (int b=2;b<=5;b++)
      for (int c = 2; c <=5; c++) {
	i2num[index][0]=a;
	i2num[index][1]=b;
	i2num[index][2]=c;
	index++;
      }
  }

  memset(prod2prob,0,sizeof(prod2prob));

  for (int i = 0; i < 64; i++) {
    for (int mask = 0; mask < 8; mask++) {
      int prod = 1;
      for (int j = 0; j < 3; j++) 
	if (mask&(1<<j)) {
	  prod *= i2num[i][j];
	}
      prod2prob[i][prod] += 1/8.;
    }
  }

  for (int i = 0; i < 64; i++)
    for (int prod = 0; prod < 126; prod++) {
      if (prod2prob[i][prod] > 0)
	prod2prob[i][prod] = log(prod2prob[i][prod]);
    }

  int T, R, N, M, K;
  cin >> T >> R >> N >> M >> K;
  
  cout << "Case #1:\n";
  for (int test = 0; test < R; test++) {
    // read K numbers
    memset(prob, 0, sizeof(prob));
    for (int k = 0; k < K; k++) {
      int x;
      cin >> x;
      for (int i = 0; i < 64; i++) {
	if (prob[i] == 1e100)
	  continue;
	prob[i] += prod2prob[i][x];
	if (prod2prob[i][x] == 0)
	  prob[i] = 1e100;
      }
    }

    int maxi = -1;
    double maxlog = -1e100;
    for (int i = 0; i < 64; i++) {
      if (prob[i] == 1e100)
	continue;
      if (maxi == -1 || maxlog < prob[i]) {
	maxi = i;
	maxlog = prob[i];
      }
    }

    int a = i2num[maxi][0];
    int b = i2num[maxi][1];
    int c = i2num[maxi][2];
    cout << a << b << c << endl;
  }

  return 0;
}
