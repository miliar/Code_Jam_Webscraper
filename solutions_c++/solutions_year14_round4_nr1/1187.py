#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <fstream>

using namespace std;

#define rep(i,n) for(int i = 0; i < (n); ++i)
#define forr(i,a,b) for(int i = (a); i <= (b); ++i)

typedef long long ll;


int main()
{
    ofstream fout("out.txt");
    freopen("in.txt","r",stdin);
	freopen("debug.txt","w",stdout);

    int t;
    cin >> t;

	int n, x;
	vector<int> vs;
	rep(tc,t)
	{
		cin >> n >> x;
		vs.resize(n);
		rep(i,n)
			cin >> vs[i];

		sort(vs.begin(), vs.end());
		int fi = 0, li = n-1;
		int ans = 0;
		while (fi < li)
		{
			if (vs[li] + vs[fi] <= x)
			{
				ans++;
				fi++;
				li--;
			} else
			{
				li--;
				ans++;
			}
		}

		if (fi == li)
			++ans;

		fout << "Case #" << tc + 1 << ": " << ans << "\n";
	}

    return 0;
}