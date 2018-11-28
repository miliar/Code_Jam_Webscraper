#include "string.h"
#include <cstring>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <map>
#include <stack>
#include <list>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <limits.h>
#include <fstream>
using namespace std;


/*void countDigitals(vector<int>& digitals, long long n, int& count)
{
	while (n > 0){

		int d = n % 10;
		if (!digitals[d]){
			digitals[d] = 1;
			++count;
		}
		n = n / 10;
	}
}

int main()
{
	int t, n;
	ifstream istream;
	istream.open("input.in");
	istream >> t;
	ofstream ostream;
	ostream.open("output.in");
	int i = 0;
	while (t--)
	{
		i++;
		istream >> n;
		if (n == 0) {
			ostream << "Case #" << i << ": " <<"INSOMNIA" << endl;
			continue;
		}
		vector<int> digitals(10, 0);
		int count = 0;
		long long digital = 0;
		while (count < 10)
		{
			digital += n;
			countDigitals(digitals, digital, count);
		}
		ostream << "Case #" << i << ": " << digital << endl;
	}
	ostream.flush();
	ostream.close();
	return 0;
}*/

/*int main()
{
	int f[101] = { 0 }; //表示以+为开头的+-+-模式串， f[i]表示长度为i的串需要的最少变换次数
	int g[101] = { 0 }; //表示以-为开头的-+-+模式串

	f[1] = 0; g[1] = 1; g[2] = 1; f[2] = 2;
	for (int i = 3; i <= 100; i++)
	{ 
		if (i % 2)
		{
			f[i] = 1 + g[i - 1];//表示翻转一次
			g[i] = 1 + f[i];
		}
		else
		{
			f[i] = 2 + f[i - 2];
			g[i] = g[i - 1];
		}
	}
	

	int t;
	ifstream istream;
	istream.open("input.in");
	istream >> t;
	ofstream ostream;
	ostream.open("output.in");
	int index = 0;
	while (t--)
	{
		index++;
		bool start_add = true;
		string str;
		istream >> str;
		
		int len = str.length();
		start_add = str[0] == '+';
		int count = 1;
		for (int i = 1; i < len; i++)
		{
			if (str[i] != str[i - 1]) count++;
		}
		cout << str << " " << count << endl;
 		int value = start_add ? f[count] : g[count];
		ostream << "Case #" << index << ": " << value << endl;
	}
	return 0;
}*/

#define MAX 33333334

bool isPrime[MAX + 1] = { 1 };
vector<int> prime;

bool check(vector<int> bits, vector<int>& v)
{
	for (int i = 2; i <= 10; i++)
	{
		long long sum = 0;
		for (int j = 0; j < bits.size(); j++) sum = sum * i + bits[j];

		bool isprime = true;
		for (int k = 0; k < prime.size() && sum > prime[k]; k++){
			if (sum % prime[k] == 0){
				v.push_back(prime[k]);
				isprime = false;
				break;
			}
		}

		if (isprime) return false;
	}

	return true;
}

void find(vector<int>& bits, int n, int& m, ofstream& ostream)
{
	if (m == 0) return;

	if (n == 0)
	{
		vector<int> v;
		if (check(bits, v)){
			for (int i = 0; i < bits.size(); i++) ostream << bits[i];
			for (int i = 0; i <= 8; i++) ostream << " " << v[i];
			ostream << endl;
			m--;
		}
	}
	else
	{
		bits[n] = 1;
		find(bits, n - 1, m, ostream);

		bits[n] = 0;
		find(bits, n - 1, m, ostream);
	}


}

int main()
{

	memset(isPrime, true, sizeof(isPrime));
	for (int i = 2; i <= MAX; i++)
	{
		if (isPrime[i]) prime.push_back(i);
		int total = prime.size();
		for (int j = 0; j < total && i * prime[j] <= MAX; j++){
			isPrime[i * prime[j]] = false;
			if (i % prime[j] == 0) break;
		}
	}

	//cout << prime.size() << endl;

	int t;
	ifstream istream;
	istream.open("input.in");
	istream >> t;

	ofstream ostream;
	ostream.open("output.in");
	int n, m;
	for (int i = 1; i <= t; i++)
	{
		istream >> n >> m;

		ostream << "Case #" << i << ":" << endl;
		vector<int> bits(n, 0);
		bits[0] = bits[n - 1] = 1;
		find(bits, n - 2, m, ostream);
	}
	ostream.flush();
	ostream.close();

	return 0;
}