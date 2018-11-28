#include <iostream>

using namespace std;

int includeNumber(long long num, int digitsPresent, bool present[])
{
  string numString = to_string(num);

  for(int i = 0; i<numString.length(); i++)
  {
    if(!present[numString[i] - '0'])
    {
      digitsPresent++;
      present[numString[i] - '0'] = true;
    }
  }

  return digitsPresent;
}

long long lastNumber(int num)
{
  if(num == 0)
    return -1;

  int digitsPresent = 0;
  int multiplier = 0;
  bool present[10] = {false};

  while(digitsPresent != 10)
  {
    multiplier++;
    digitsPresent = includeNumber(num*multiplier, digitsPresent, present);
  }
  return num*multiplier;
}

int main()
{
	int t, n;
  cin >> t;
  for(int i = 1; i <= t; i++)
  {
  	cin >> n;
  	if(n == 0)
  		cout << "Case #" << i << ": INSOMNIA" << endl;
  	else
  		cout << "Case #" << i << ": " << lastNumber(n) << endl;
  }

  return 0;
}