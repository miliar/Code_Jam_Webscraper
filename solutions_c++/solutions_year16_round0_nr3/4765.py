#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>

using namespace std;

bool isPrime(const uint64_t n, uint64_t& factor)
{
  if (n <= 1)
    {
      factor = 1;
      return false;
    }
  else if (n <= 3)
    {
      factor = 0;
      return true;
    }
  else if (n % 2 == 0)
    {
      factor = 2;
      return false;
    }
  else if (n % 3 == 0)
    {
      factor = 3;
      return false;
    }
  uint64_t i = 5;
  while (i*i <= n)
    {
      if (n % i == 0)
	{
	  factor = i;
	  return false;
	}
      else if (n % (i + 2) == 0)
	{
	  factor = i + 2;
	  return false;
	}
      i += 6;
      if (i >= 4294967296)
	{
	  factor = 0;
	}      
    }
  factor = 0;
  return true;
}

vector<string> generateGrayarr(int n)
{
  vector<string> arr;
 
  arr.push_back("0");
  arr.push_back("1");
 
  // Every iteration of this loop generates 2*i codes from previously
  // generated i codes.
  int i, j;
  for (i = 2; i < (1<<n); i = i<<1)
    {
      // Enter the prviously generated codes again in arr[] in reverse
      // order. Nor arr[] has double number of codes.
      for (j = i-1 ; j >= 0 ; j--)
	arr.push_back(arr[j]);
 
      // append 0 to the first half
      for (j = 0 ; j < i ; j++)
	arr[j] = "0" + arr[j];
 
      // append 1 to the second half
      for (j = i ; j < 2*i ; j++)
	arr[j] = "1" + arr[j];
    }

  return arr;
}

void generateJamCoin(int jamCoin[], vector<string> arr)
{
  static unsigned i = 0;
  int j = 1;
  for (auto c : arr[i])
    {
      jamCoin[j] = c-'0';
      j++;
    }
  i = (i + 1) % arr.size();
}

uint64_t toBase(int jamCoin[], const int& N, int base)
{
  uint64_t valueInDec = 0;
  for(int i = 0; i < N; ++i)
    {
      valueInDec += jamCoin[i]*pow(base,i);
    }
  return valueInDec;
}

int main(int argc, char* argv[])
{
  /**
   * Static
   */
  if(argc != 2)
    {
      cerr << "argc != 2" << '\n';
      return 0;
    }

  ifstream infile;
  infile.open (argv[1]);

  string inputLine;
  uint32_t numCases;
  getline(infile, inputLine);
  stringstream ss(inputLine);

  unsigned N, J;
  
  ss >> numCases;
  
  getline(infile, inputLine);
  stringstream ss1(inputLine);

  ss1 >> N;
  ss1 >> J;

  /**
   * Fileread
   */
  //int value;
  //vector<vector<int> > data;
  //string substring;
  //vector <string> stringVec;
  //vector <vector <string> > string2DVec;
  /*
  while(getline(infile, inputLine))
    {
      stringVec.push_back(inputLine);
    }
  */
  /*
  cout << "stringVec: " << endl;
  for_each (stringVec.begin(), stringVec.end(), printAll);
  cout << endl;
  */
  infile.close();

  /**
   * Problem
   */

  int jamCoin[32] = {0};
  jamCoin[0] = 1;
  jamCoin[N-1] = 1;
  uint64_t coinArray[9];
  uint64_t factorArray[9];
  bool findJamCoin = true;

  static vector<string> arr = generateGrayarr(N-2);


  cout << "Case #" << numCases << ":" << endl;

  for(unsigned i = 0; i < J; ++i)
    {
      findJamCoin = true;
	  
      while(findJamCoin)
	{
	  generateJamCoin(jamCoin, arr);

	  for (int base = 2; base < 11; base++)
	    {
	      coinArray[base-2] = toBase(jamCoin, N, base);
	      if (isPrime(coinArray[base-2], factorArray[base-2]))
		{
		  findJamCoin = true;
		  break;
		}
	      findJamCoin = false;
	    }
	}
      for(int coin = N-1; coin >= 0; coin--)
	{
	  cout << jamCoin[coin];
	}
	  
      for(int factor = 0; factor < 9; factor++)
	{
	  cout << " " << factorArray[factor];
	}
      cout << endl;
      /*
	for(int i = 0; i < 9; i++)
	{
	cout << " " << coinArray[i][0];
	}
	cout << endl;
      */
    }
    

  return 0;
}
