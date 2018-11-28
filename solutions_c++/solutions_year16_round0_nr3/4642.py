#include <iostream>
#include <math.h>

using namespace std;

long long smallestNTDivisor(long long num)
{
  if(num%2 == 0)
    return 2;

  int r = sqrt(num);
  for(int i = 3; i<=r; i++)
  {
    if(num%i == 0)
      return i;
  }
  return -1;
}

string convertToBase2(int num)
{
  string binary = bitset<32>(num).to_string();
  binary.erase(0,binary.find_first_of('1'));
  return binary;
}

long long convertToBase10(string num, int base)
{
  long long num10 = 0;
  for(int i = 0; i<num.length(); i++)
  {
    num10 += (num[num.length()-1-i]-'0')*pow(base,i);
  }
  return num10;
}

bool isJamcoin(long long num)
{
	bool jamcoin = true;
  string binary = convertToBase2(num);
  for(int i = 2; i <= 10 && jamcoin; i++)
  {
  	if(smallestNTDivisor(convertToBase10(binary, i)) == -1)
  		jamcoin = false;
  }
  return jamcoin;
}

void findJamcoins(int n, int j)
{
  int found = 0;
  long long num = 32769;
  if(n == 32)
  	num = 2147483649;

  while(found < j)
  {
  	if(isJamcoin(num))
  	{
  		string binary = convertToBase2(num);
  		cout << binary;
  		for(int i = 2; i <= 10; i++)
  		{
  			cout << " " << smallestNTDivisor(convertToBase10(binary, i));
  		}
  		cout << endl;
  		found++;
  	}
  	num+=2;
  }
}

int main()
{
  int t, n, j;
  cin >> t;
  for(int i = 1; i <= t; i++)
  {
  	cin >> n >> j;
    cout << "Case #" << i << ": " << endl;
    findJamcoins(n,j);
  }
}