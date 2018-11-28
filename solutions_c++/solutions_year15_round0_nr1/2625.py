#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;
using pii = pair<int, int>;
using vi = vector<int>;
using ll = long long;

#define rep(i,n) for(int i=0; i<n; i++) 
#define repa(i,s,e) for(int i=s; i<=e; i++)
#define repd(i,s,e) for(int i=s; i>=e; i--)

int solve(const vi& s)
{
	if (s.size() <= 1)
	{
		return 0;
	}

	int result = 0;
	int sum = 0;

	for (int i = 0; i < s.size(); i++)
	{
		int num = s[i];

		if (num > 0 && sum < i)
		{
			result += (i - sum);
			sum += (i - sum);
		}

		sum += num;
	}

	return result;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		int Smax;
		std::vector<int> Svec;

		std::string Sstring;
		cin >> Smax >> Sstring;

		for (char c : Sstring)
		{
			Svec.emplace_back(c - '0');
		}

		cout << "Case #" << (i + 1) << ": " << solve(Svec) << endl;
	}
}
