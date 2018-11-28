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
int n;
VI v, u;


void print(VI v) {
	for(int i = 0; i < sz(v); i++)	cout << v[i] << ' ';
	cout << "\n\n";
}


int main(int argc, char const *argv[])
{
	cin >> t;

	for (int cs = 0; cs < t; ++cs)
	{
		cin >> n;
		v = VI(n);
		for (int i = 0; i < n; ++i) {
			cin >> v[i];
		}
		u = v;
		sort(all(u));
		int ans = 0, pos;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n-i; ++j)
			{
				if(v[j] == u[i]) {
					pos = j;
					break;
				}
			}
			ans += min(pos - 0, n - i - 1 - pos);
			v.erase(v.begin()+pos);
		}
		cout << "Case #" << cs+1 << ": " << ans << '\n';
	}
	return 0;
}