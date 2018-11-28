#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

struct Pol
{
	Pol(int a1, long long a21)
		: a(a1)
		, a2(a21)
	{
	//	cout << a << ' ' << a2 << endl;
	}

	int a;
	long long a2;
};

bool operator<(const Pol& p1, const Pol& p2)
{
	return p1.a < p2.a;
}

std::vector<Pol> a;
std::vector<int> d;

bool isPol(long long a)
{
	unsigned i;
	d.clear();
	while(a)
	{
		d.push_back(a%10);
		a/=10;
	}
	for(i=0; i<d.size();++i)
		if(d[i] != d[d.size()-1-i])
			return false;

	return true;
}

int cP1(int n)
{
	int ans = n;
	n /= 10;
	while(n)
	{
		ans *= 10;
		ans += n%10;
		n/=10;
	}
	return ans;
}

int cP2(int n)
{
	int ans = n;
	while(n)
	{
		ans *= 10;
		ans += n%10;
		n/=10;
	}
	return ans;
}

void calcAll()
{
	int i;
	for(i=1;i<=99999;++i)
	{
		int n1 = cP1(i);
		long long n12 = (long long) n1 * (long long)n1;
		if(isPol(n12))
			a.push_back(Pol(n1, n12));

		int n2 = cP2(i);
		long long n22 = (long long) n2 * (long long)n2;
		if(isPol(n22))
			a.push_back(Pol(n2, n22));
	}
}

int main()
{
	unsigned i;
    calcAll();
	sort(a.begin(), a.end());
	//for(i=0; i<a.size(); ++i)
	//	cout<<a[i].a << ' '<<a[i].a2<<endl;
	int t, tt;
	long long A, B;
	fin>>tt;
	for(t=1; t<=tt; ++t)
	{
		fin>>A>>B;
		int count = 0;
		for(i=0; i<a.size(); ++i)
			if(a[i].a2>= A && a[i].a2<=B)
				++count;

		fout << "Case #" << t<<": " << count<<endl;
	}

	return 0;
}