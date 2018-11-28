#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

struct test
{
	 int n;
	 int j;
};
vector<test> readFromFile()
{
	vector<test> input;
	ifstream fin ("input.txt");
	int count;
	fin >> count;
	for (int i = 0; i < count; ++i)
	{
		input.push_back(test());
		fin >> input[i].n;
		fin >> input[i].j;

		//input.push_back(t);
		//cout << input[i].n << " " << input[i].j << endl;

	}
	return input;
}
vector<int> getBin(int n)
{
	vector<int> v;
	while (n>0)
	{
		int cur = n % 2;
		v.push_back(cur);
		n /= 2;
	}
	reverse(v.begin(), v.end());
	return v;
}
vector<unsigned long long> getSystems(vector<int> v)
{
	vector<unsigned long long> rez = {0,0,0,0,0,0,0,0,0} ;
	for (auto elem : v)
	{
		for (int j = 2; j <= 10; j++)
		{
			rez[j - 2] = rez [j - 2] * j + elem;
		}
	}
	return rez;
}
inline bool IsPrime(unsigned long long number )
{
 	if ( ( (!(number & 1)) && number != 2 ) || (number < 2) || (number % 3 == 0 && number != 3) )
  		return (false);

 for( int k = 1; 36*k*k-12*k < number;++k)
  if ( (number % (6*k+1) == 0) || (number % (6*k-1) == 0) )
   return (false);
  return true;
 }
 inline bool NotPrime(int number)
 {
 	if ((number != 2 && number != 3 && number != 5) && (number % 2 == 0 || number % 3 ==0 || number % 5 == 0 )) return true;
 	return false;
 }
bool AllNotPrime(vector<unsigned long long> v)
{
	for (auto elem : v)
	{
		if (IsPrime(elem)) return false;
	}
	return true;

}
unsigned long long getFirnP(unsigned long long n)
{
	for (int i = 2; i < n; ++i)
	{
		if (n % i == 0) return i;
	}
}
string getnamefromv(vector<int> v)
{
	string s = "";
	for(auto elem : v)
		s+=to_string(elem);
	return s;
}
void generate(int n, int j, ofstream &  fout)
{
	int i = 1;
	int start = pow(2, n - 1) + 1;
	while (i <= j &&  start < pow(2, n))
	{
		auto v = getBin(start);
		auto s = getSystems(v);
		if (v[n - 1] == 1 && AllNotPrime(s))
		{
			fout << getnamefromv(v) << " " << getFirnP(s[0]) << " " << getFirnP(s[1]) << " " << getFirnP(s[2]) 
			<< " " << getFirnP(s[3]) << " " << getFirnP(s[4]) << " " << getFirnP(s[5]) << " " << getFirnP(s[6])
			<< " " << getFirnP(s[7]) << " " << getFirnP(s[8]) << endl;
			i++;
		}
		start++;
	}



}


int main()
{
	ofstream fout("output.txt");
	auto tests = readFromFile();
	for (int i = 0; i < tests.size(); ++i)
	{
		fout << "Case #" << i + 1 << ":" << endl;
		generate(tests[i].n, tests[i].j, fout);
	}
	return 0;
}