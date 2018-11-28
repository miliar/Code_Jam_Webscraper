#include <iostream>
using namespace std;

int main() {
  unsigned long long int Ni[100], T;
  cin >> T;
  for (int i = 0; i < T; i++)
    cin >> Ni[i];

  int k = 0;
  unsigned long long int N;
  for (int i = 0; i < T; i++) {
    N = Ni[k];
    int arr[10];
    int count = 1;
    for (int j = 0; j < 10; j++)
      arr[j] = 0;
    int found = 1;
    while (1) {
      unsigned long long int tmpN = N*count;
      if (tmpN <= 0) {
	found = 0;
	break;
      }
      while (tmpN > 0) {
	arr[tmpN % 10] = 1;
	tmpN /= 10;
      }
      int flag = 1;
      for (int j = 0; j < 10; j++)
	if (arr[j] == 0)
	  flag = 0;
      if (flag)
	break;
      count++;
    }
    if (found) {
      cout << "Case #" << i+1 << ": " << count*N << endl;
    } else {
      cout << "Case #" << i+1 << ": INSOMNIA" << endl;
    }
    k++;
    if (k == T)
      break;
  }
  return 0;
}
