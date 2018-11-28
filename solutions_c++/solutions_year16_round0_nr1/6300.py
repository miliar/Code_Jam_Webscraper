#include <iostream>
using namespace std;

int digit;
int count(int N);

int main()
{
  unsigned C;
  cin>>C;
  int N;

  for(int i=0; i<C; ++i) {
    digit = 0;
    cin >> N;

    if (N == 0) {
      cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
      continue;
    }

    cout<<"Case #"<<i+1<<": "<<count(N)<<endl;
  }

  return 0;
}

int count(int N)
{
  int sum = N;

  while (true) {
    int temp = sum;

    while(temp > 0) {
      digit |= (1<<temp%10);
      temp /= 10;

      if (digit == 1023)
        return sum;
    }

    sum += N;
  }

  return sum;
}