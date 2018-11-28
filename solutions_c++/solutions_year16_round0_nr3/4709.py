#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;
const int INF = 2147483647;

long long tobase(string, int);
int main()
{
	int t;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> t;
	for (int times = 1; times <= t; times++)
	{
		fout << "Case #1: " << endl;
		vector <int> primes;
		for (int i = 2; i < 1000; i++)
		{
			int prime = true;
			for (int j = 2; j <= sqrt(i) && prime; j++)
				if ((i%j) == 0)
					prime = false;
			if (prime)
				primes.push_back(i);
		}
		int n, j;
		fin >> n >> j;
		string zeroes(n-2,'0');
		//long long num = 1000000000000001;
		//cout << num << endl;
		int found = 0;
		string current = zeroes;
		while (found < j)
		{
			string num = '1' + current + '1';
			vector<long long> nums;
			vector <int> divisors;
			for (int i = 2; i <= 10; i++)
				nums.push_back(tobase(num, i));
			//cout << num << endl;
			bool notprime = true;
			for (int i = 0; i < nums.size(); i++)
			{
				bool nprime = false;
				for (int j = 0; j < primes.size(); j++)
				{
					if ((nums[i] % primes[j]) == 0)
					{
						nprime = 1;
						divisors.push_back(primes[j]);
						break;
					}
				}
				if (!nprime)
				{
					notprime = false;
					break;
				}
			}
			if (notprime)
			{
				found++;
				fout << num;
				for (int i = 0; i < divisors.size(); i++)
					fout << " " << divisors[i];
				fout << endl;
			}
			
			int i = current.size() - 1;
			while (current[i] == '1')
			{
				current[i] = '0';
				i--;
			}
			current[i] = '1';
		}
		//cout << "Case #" << times << ": " << endl;
	}
	cin.get();
	return 0;
}

long long tobase(string s, int b)
{
	int long long num = 0;

	for (int i = s.size() - 1,power = 0; i >= 0; i--,power++)
		num += (s[i] - '0')*pow(b, power);
	return num;
}