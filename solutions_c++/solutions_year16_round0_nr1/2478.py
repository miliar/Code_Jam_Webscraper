#include <fstream>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <iomanip>
#pragma comment(linker, "/STACK:200000000")
using namespace std;
bool digits[10];
bool check()
{
	bool ok = true;
	for (int i = 0; i < 10; ++i)
		if (!digits[i])
			ok = false;
	return ok;
}
void getdigits(long long n)
{
	while (n > 0ll)
	{
		digits[n % (10ll)] = true;
		n /= 10ll;
	}
}
int main()
{
	ifstream in("A-large.in");
	ofstream out("small.out");
	int tests;
	long long n;
	in >> tests >> ws;
	for (int t = 1; t <= tests; ++t)
	{
		
		in >> n;
		for (int i = 0; i < 10; ++i)
			digits[i] = false;
		if(n==0ll)
			out << "Case #" << t << ": " << "INSOMNIA" << endl;
		else
		{
			long long i = 1ll;
			for (; !check(); ++i)
			{
				getdigits(n*i);
			}
			out << "Case #" << t << ": " << n*(i-1ll) << endl;
		}
		
	}

	//system("pause");
	in.close();
	out.close();
	return 0;
}