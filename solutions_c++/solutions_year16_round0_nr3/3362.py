#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
using namespace std;

bool prime[400000050];
vector <int> primes;
void sieve (int N)
{
	memset(prime,1,sizeof prime);
	prime[1] = prime[0] = 0;
	for (long long i=2 ; i<=N ; i++)
	{
		if (!prime[i]) continue;
		for (long long j = i*i ; j<=N ; j+=i)
			prime[j] = 0;
		primes.push_back(i);
	}
}

vector <long long> fromBases (string s)
{
	vector <long long> ret (11);
	long long POW[11];
	for (int i=0 ; i<=10 ; i++) POW[i] = 1LL;

	for (int i=s.size()-1, j=0 ; i>=0 ; i--,j++)
	{
		for (int j=2 ; j<=10 ; j++)
		{
			ret[j] += (s[i] - '0') * POW[j];
			POW[j] *= j;
		}
	}

	return ret;
}

string s;
vector <string> list;
void getStrings (int i)
{
	if (i == 0)
	{
		string ret = "1";
		ret += s;
		ret += '1';
		list.push_back(ret);
		return;
	}

	s[i] = '0';
	getStrings(i-1);
	s[i] = '1';
	getStrings(i-1);
	return;
}

int getFactor (long long N)
{
	for (int i=2 ; i<primes.size() && primes[i] < N ; i++)
		if (N%i == 0) return i;
	return -1;
}
int main ()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	sieve(400000010);

	int TC;
	cin >> TC;
	int CC = 1;
	while (TC--)
	{
		printf("Case #%d:\n",CC++);
		int N,J;
		cin >> N >> J;

		s.clear();
		for (int i=0 ; i<N-2 ; i++) s += '0';
		getStrings(N-2);

		for (int i=0 ; i<list.size() && J ; i++)
		{

			bool prime1 = 0, prime2 = 0;
			vector <long long> v = fromBases(list[i]);
			for (int j=2 ; j<v.size() ; j++)
			{
				if (getFactor(v[j]) == -1) prime2 = 1;
			}

			if (!prime2)
			{
				cout << list[i];
				for (int j=2 ; j<v.size() ; j++)
				{
					cout << " " << getFactor(v[j]);
				}
				cout << endl;
				J--;
			}
		}

	}
}