#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

#define rep(i,n) for(int i = 0; i < (n); ++i)
#define forr(i,a,b) for(int i = (a); i <= (b); ++i)

typedef long long ll;

typedef int m4x4[4][4];

int solve(int r1, const m4x4& a1, int r2, const m4x4& a2)
{
	set<int> fr;
	rep(i,4)
		fr.insert(a1[r1-1][i]);

	int cnt = 0, ans;
	rep(i,4)
		if (fr.find(a2[r2-1][i]) != fr.end())
		{
			ans = a2[r2-1][i];
			cnt++;
		}

	return cnt == 1 ? ans : (cnt == 0 ? 0 : -1);
}

int main()
{
#ifdef my_env_def
    freopen ("out.txt","w",stdout);
    freopen("in.txt","r",stdin);
#endif

    int t;
    cin >> t;

	m4x4 a1, a2;
	int r1, r2;

	rep(tc,t)
	{
		cin >> r1;
		rep(i,4)
			rep(j,4)
				cin >> a1[i][j];

		cin >> r2;
		rep(i,4)
			rep(j,4)
				cin >> a2[i][j];

		int ans = solve(r1,a1, r2,a2);
		
		if (ans > 0)
			cout << "Case #" << tc + 1 << ": " << ans << "\n";
		else
			cout << "Case #" << tc + 1 << ": " << (ans == -1 ? "Bad magician!" : "Volunteer cheated!") << "\n";
	}

#ifdef my_env_def
    fclose(stdout);
#endif
    return 0;
}