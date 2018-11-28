#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <functional>
#include <algorithm>
using namespace std;

typedef long long ll;
#define MOD 1000000007

int main(void)
{
	std::ios_base::sync_with_stdio(false);

	int t, i;
	ll a, b;
	ll sp[] =
	{
		1ll,
		4ll,
		9ll,
		121ll,
		484ll,
		10201ll,
		12321ll,
		14641ll,
		40804ll,
		44944ll,
		1002001ll,
		1234321ll,
		4008004ll,
		100020001ll,
		102030201ll,
		104060401ll,
		121242121ll,
		123454321ll,
		125686521ll,
		400080004ll,
		404090404ll,
		10000200001ll,
		10221412201ll,
		12102420121ll,
		12345654321ll,
		40000800004ll,
		1000002000001ll,
		1002003002001ll,
		1004006004001ll,
		1020304030201ll,
		1022325232201ll,
		1024348434201ll,
		1210024200121ll,
		1212225222121ll,
		1214428244121ll,
		1232346432321ll,
		1234567654321ll,
		4000008000004ll,
		4004009004004ll
	};
	vector<ll> list(sp, sp+39);

	fstream input("C-large-1.in", fstream::in);
	fstream output("output.txt", fstream::out | fstream::trunc);

	string line;
	string::iterator itr;
	stringstream stream;

	getline(input, line);
	stream.clear();
	stream << line;
	stream >> t;

	for(i=1; i<=t; ++i)
	{
		getline(input, line);
		stream.clear();
		stream << line;
		stream >> a >> b;

		output << "Case #" << i << ": " << distance(list.begin(), upper_bound(list.begin(), list.end(), b)) - distance(list.begin(), upper_bound(list.begin(), list.end(), a-1)) << endl;
	}

	return 0;
}