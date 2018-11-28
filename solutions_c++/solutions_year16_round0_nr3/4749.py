#include <iostream>
#include <math.h>

using namespace std;

unsigned long long int getVal(int arr[], int base, int N) {
  unsigned long long int sum = 0;
  for (int i = N-1; i >= 0; i--) {
    if (arr[i] == 1)
      sum += pow(base, N-1-i);
  }

  return sum;
}

int getnext(int arr[], int N) {
  int flag = 0;
  for (int i = N-2; i > 0; i--) {
    if ((arr[i] == 0) && (i == N-2)) {
      arr[i] = 1;
      flag = 1;
      break;
    } else if (arr[i] == 0) {
      arr[i] = 1;
      for (int j = i + 1; j < N-1; j++)
	arr[j] = 0;
      flag = 1;
      break;
    }
  }
  if (flag)
    return 0;
  else
    return -1;
}

int primeEval(unsigned long long int num) {
  if (!(num & 1))
    return 2;
  for (int i = 3; i*i <= num; i += 2) {
    if (num % i == 0)
      return i;
  }
  return -1;
}

void printarr(unsigned long long int arr[], int N) {
  for (int i = 0; i < N; i++)
    cout << arr[i] << " ";
}

void printcoin(int arr[], int N) {
  for (int i = 0; i < N; i++)
    cout << arr[i];
}

int evaluate(int arr[], int N) {
  int flag = 1;
  unsigned long long int comp_vals[9];

  unsigned long long int num;
  for (int i = 2; i <= 10; i++) {
    if ((num = primeEval(getVal(arr, i, N))) == -1) {
      flag = 0;
      break;
    }
    comp_vals[i-2] = num;
  }

  if (flag) {
    printcoin(arr, N);
    cout << " ";
    printarr(comp_vals, 9);
    cout << endl;
    return 1;
  }
  return 0;
}

int main() {
  int arr[16];
  int T, J, N;
  cin >> T;
  cin >> N >> J;

  for (int i = 0; i < N; i++)
    arr[i] = 0;
  arr[0] = 1;
  arr[N-1] = 1;

  int count = 0;
  cout << "Case #1:" << endl;
  do {
    if (count == J)
      break;
    if (evaluate(arr, N) == 1)
      count++;
  } while (getnext(arr, N) != -1);
  return 0;
}
