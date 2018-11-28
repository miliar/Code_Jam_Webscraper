#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

bool all_true(bool *A)
{
  for (int i = 0; i < 10; ++i)
  {
    if (!A[i])
      return false;
  }
  return true;
}

void update_array(int N, bool *A)
{
  while (N)
  {
    A[N%10] = true;
    N /= 10;
  }
  return;
}

string time_to_sleep(int N)
{
  if (N == 0)
    return string("INSOMNIA");
  bool *A = (bool *) malloc(sizeof(bool)*10);
  for (int i = 0; i < 10; ++i)
  {
    A[i] = false;
  }
  int count = 0;
  while (!all_true(A))
  {
    count += N;
    update_array(count, A);
  }
  free(A);
  char str[33];
  sprintf(str, "%d", count);
  return string(str);
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t)
  {
    int N;
    cin >> N;
    cout << "Case #" << t << ": " << time_to_sleep(N) << endl;
  }
}
