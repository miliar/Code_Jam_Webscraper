#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>
using namespace std;
#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(a) (int)(a.size())
#define all(a) a.begin(), a.end()
#define R(a) ((a)%mod)

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;

int t;
int n, x;
VI v;

int main(int argc, char const *argv[])
{
	cin >> t;

	for (int cs = 0; cs < t; ++cs)
	{
		cin >> n >> x;
		v = VI(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i];
		}
		sort(all(v));
		int j = 0, cnt = 0;
		for (int i = n-1; j < i; --i)
		{
			if(v[i] + v[j] <= x)	cnt++, j++;
		}
		cout << "Case #" << cs+1 << ": " << n - cnt << '\n';
	}
	return 0;
}