#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;
typedef unsigned long long ull;

bool isPalin(const ull &A)
{
	ull a = A;
	vector<char> didgits;

	while(a)
	{
		didgits.push_back(a % 10);
		a/=10;
	}
	bool res = true;
	for(int i=0, k=didgits.size()-1; i<k && res; i++, k--) res = didgits[i] == didgits[k];

	return res;
}


int main()
{
	ios::sync_with_stdio(0);
	int t, n = 0;
	cin >> t;
	
	while(t--)
	{
		n++;
		int ans = 0;
		ull a, b;
		cin >> a >> b;

		ull begin = (ull)(ceil(sqrt(a)));
		ull end = (ull)sqrt(b);

		for(int i=begin; i<=end; i++) ans += isPalin(i)&&isPalin(i*i);

		cout << "Case #" << n << ": " << ans << endl;
	}

	return 0;
}