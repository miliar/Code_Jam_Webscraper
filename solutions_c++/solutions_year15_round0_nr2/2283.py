#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <hash_map>
#include <unordered_set>


using namespace std;
typedef long long ll;

vector<int> v;


int check(int m)
{
	int ans = 0;
	for (int i = 0; i < v.size(); ++i)
	{
		if (v[i] > m)
		{
			ans += ((v[i]+m -1) / m - 1);
		}
	}
	return ans + m;

}
int main(){
	freopen("B-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	srand(time(NULL));
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		
		int n;
		cin >> n;
		v.clear();
		int mx = -1;
		for (int i = 0; i < n; ++i)
		{
			int q;
			cin >> q;
			//q = rand() % 1000;
			v.push_back(q);
			mx = max(mx, q);
		}
		int ans = 1e9;
		for (int m = 1; m <= mx; ++m)
		{
			ans = min(check(m), ans);
		}

		cout <<"Case #"<<t<<": "<< ans << endl;
	}


	return 0;
}