#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cstdio>
#include <map>
using namespace std;
vector<long long> pals;
bool is_palindrom(long long i)
{
	vector<int> v1, v2; 
	v1.reserve(20);
	v2.reserve(20);
	while(i)
	{
		v1.push_back(i % 10);
		i /= 10;
	}
	v2 = v1;
	reverse(v2.begin(), v2.end());
	return v1 == v2;
}
void generate()
{
	for (long long i = 1; i < 1000 * 1000 * 10; i++)
		if (is_palindrom(i) && is_palindrom(i * i))
			pals.push_back(i * i);



}
long long solve()
{
	long long a, b;
	cin >> a >> b;
	long long ans = 0;
	for (int i = 0; i < pals.size(); i++)
	{
		if (pals[i] <= b && pals[i] >= a)
			ans++;
	}
	return ans;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	generate();
	int test = 0;
	cin >> test;
	for (int iT = 0; iT < test; iT++)
	{
		printf("Case #%d: %lld\n", iT+1, solve());
	}
	return 0;
}