#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>
using namespace std;

unsigned long long int pows(const unsigned long long int n, int base)
{
  unsigned long long int ans = 1;
  for(int i = 0; i < base; i++)
    ans = ans * n;
  return ans;
}

void printJama(vector <bool> & v)
{
  for(int i = 0; i < v.size(); i++)
    cout << v[i];
  return;
}

unsigned long long int testForPrimes(unsigned long long int value, vector<unsigned long long int > & primes)
{
  for(int i = 0; i < primes.size(); i++)
  {
	if(primes[i] > sqrt(value))
	  return 0;
    if((value % primes[i]) == 0)
	  return primes[i];
  }
}

bool increment(vector <bool> & v)
{
  bool carry = 1;
  for(int i = v.size() - 1; i >= 0; i--)
  {
	if(v[i] == 1)
	  v[i] = 0;
    else
	{
	  v[i] = 1;
	  carry = 0;
	}
	if(carry == 0)
	  break;
  }
  if(carry == 1)
    return false;
  else
	return true;
}

unsigned long long int getvalue(vector <bool> & v, const int base)
{
  int counter = 0;
  unsigned long long int value = 0;
  for(int i = v.size() - 1; i >= 0; i--)
  {
	value = value + int(v[i]) * pows(base, counter);
	counter++;
  }
  return value;
}

int main()
{
  const int lb = 2; //lowest base
  const int hb = 10; //high base
  const int numJ = 50; //max number of jama coins
  const int lengthJ = 16; //length of jama coins
  vector<unsigned long long int > primes;
  vector<unsigned long long int > divsors;
  int counter;
  int k; //iterator
  vector<bool> v;
  bool exausted;
  bool isCoin;
  unsigned long long int value10;
  ifstream fin;
  
  divsors.resize(hb - lb + 1);
  fin.open("primes.txt");
  fin >> value10;
  while(fin)
  {
	primes.push_back(value10);
	fin >> value10;
  }
  fin.close();
  
  for(int i = 2; i <= lengthJ; i++)
  {
	counter = 0;
	exausted = false;
	v.resize(i);
	v[0] = 1;
	for(int j = 1; (j < lengthJ - 1); j++)
	  v[j] = 0;
    v[i - 1] = 1;
	while(counter < numJ && !exausted)
	{
	  isCoin = true;
	  k = 0;
	  for(int j = lb; j <= hb; j++)
	  {
		value10 = getvalue(v,j);
		divsors[k] = testForPrimes(value10, primes);
		if(divsors[k] == 0)
		{
		  isCoin = false;
		  break;
		}
		k++;
	  }
	  if(isCoin)
	  {
	    printJama(v);
		cout << " ";
		for(int j = 0; j < (hb - lb + 1); j++)
		  cout << divsors[j] << " ";
	    cout << endl;
		counter++;
	  }
	  for(int j = 0; j < 2; j++)
	  {
	    exausted = !increment(v);
		if(exausted)
		  break;
	  }
	}
  }
  return 0;
}