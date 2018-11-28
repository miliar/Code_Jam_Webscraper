#include <algorithm>
#include <tuple>
#include <vector>
#include <string>
#include <iostream>
using namespace std;
using ll = unsigned long long;

#include <fstream>

void work(ll t)
{
	static int tc = 1;
	ofstream file;
	file.open("output_large.txt", ios::out | ios::app);
	ll answer = (1 << 10) - 1;
	int current = 0;
	ll c = 1;
	if (t == 0)
	{
		file << "Case #" << tc++ << ": " << "INSOMNIA" << endl;
		return;
	}
	ll ip = t;
	while (current != answer)
	{
		ll q = t*c;
		while (q > 0)
		{
			auto p = q % 10;
			current |= (1 << p);
			q /= 10;
		}
		++c;
	}
	file << "Case #" << tc++ << ": " << t*(c - 1) << endl;
}
int main()
{
	int n;
	cin >> n;
	while (n--)
	{
		ll i;
		cin >> i;
		work(i);
	}
}